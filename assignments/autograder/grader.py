import pandas as pd
import numpy as np
import os
import ast
import sys
import re
from glob import glob
import io
import types
from IPython import get_ipython
from nbformat import read
from IPython.core.interactiveshell import InteractiveShell





###########
#source: https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Importing%20Notebooks.html
def find_notebook(fullname, path=None):
    """find a notebook, given its fully qualified name and an optional path

    This turns "foo.bar" into "foo/bar.ipynb"
    and tries turning "Foo_Bar" into "Foo Bar" if Foo_Bar
    does not exist.
    """
    name = fullname.rsplit('.', 1)[-1]
    if not path:
        path = ['']
    for d in path:
        nb_path = os.path.join(d, name + ".ipynb")
        if os.path.isfile(nb_path):
            return nb_path
        # let import Notebook_Name find "Notebook Name.ipynb"
        nb_path = nb_path.replace("_", " ")
        if os.path.isfile(nb_path):
            return nb_path

class NotebookLoader(object):
    """Module Loader for Jupyter Notebooks"""
    def __init__(self, path=None):
        self.shell = InteractiveShell.instance()
        self.path = path

    def load_module(self, fullname):
        """import a notebook as a module"""
        path = find_notebook(fullname, self.path)

        print ("importing Jupyter notebook from %s" % path)

        # load the notebook object
        with io.open(path, 'r', encoding='utf-8') as f:
            nb = read(f, 4)


        # create the module and add it to sys.modules
        # if name in sys.modules:
        #    return sys.modules[name]
        mod = types.ModuleType(fullname)
        mod.__file__ = path
        mod.__loader__ = self
        mod.__dict__['get_ipython'] = get_ipython
        sys.modules[fullname] = mod

        # extra work to ensure that magics that would affect the user_ns
        # actually affect the notebook module's ns
        save_user_ns = self.shell.user_ns
        self.shell.user_ns = mod.__dict__

        try:
          for cell in nb.cells:
            if cell.cell_type == 'code':
                # transform the input to executable Python
                code = self.shell.input_transformer_manager.transform_cell(cell.source)
                # run the code in themodule
                exec(code, mod.__dict__)
        finally:
            self.shell.user_ns = save_user_ns
        return mod

class NotebookFinder(object):
    """Module finder that locates Jupyter Notebooks"""
    def __init__(self):
        self.loaders = {}

    def find_module(self, fullname, path=None):
        nb_path = find_notebook(fullname, path)
        if not nb_path:
            return

        key = path
        if path:
            # lists aren't hashable
            key = os.path.sep.join(path)

        self.loaders[key] = NotebookLoader(path)
        return self.loaders[key]

sys.meta_path.append(NotebookFinder())
###########




def extract_assignment(dir):
    pattern = r'([a-z\-]+)-((([0-9]{2,4})-){5}[0-9]{2,4})'
    assignment = re.findall(pattern, os.path.split(dir)[1])[0][0]
    return assignment.lower()

def get_students(submissions_dir):
    return [os.path.split(g)[1] for g in glob(os.path.join(submissions_dir, '*'))]

def notebook_to_module(target):
    if target in sys.modules:
        sys.modules.pop(target)
    exec(f'import {target} as submission', globals())
    
    return submission


def grade(x, rubric):    
    if type(rubric) == list:
        passed = []
        failed = []
        for r in rubric:
            next_passed, next_failed = grade(x, r)
            passed.extend(next_passed)
            failed.extend(next_failed)
        return passed, failed
    
    r = pd.read_excel(rubric, header=0)
    
    passed = []
    failed = []
    
    for i in range(r.shape[0]):
        next_test = {}
        if r.loc[i]['function'] == 'identity':
            next_test['cmd'] = f"x.{r.loc[i]['args']} == {r.loc[i]['solution']}"
            next_test['target'] = True
        else:
            r.at[i, 'args'] = [eval(f"{r.loc[i]['args']}")]
            
            if type(r.loc[i]['kwargs']) != dict:
                next_kwargs = '{}'
            else:
                next_kwargs = r.loc[i]['kwargs']
            
            next_test['cmd'] = f"x.{r.loc[i]['function']}(*{r.loc[i]['args']}, **{next_kwargs})"
            next_test['target'] = eval(f"{r.loc[i]['solution']}")
        next_test['points'] = float(r.loc[i]['points'])
        next_test['rubric'] = rubric
        
        try:
            next_test['response'] = eval(next_test['cmd'])   
        except:
            next_test['response'] = None        
        try:            
            if next_test['response'] == next_test['target']:
                passed.append(next_test)
            else:
                failed.append(next_test)
        except:
            try:
                if np.isnan(next_test['target']):
                    passed.append(next_test)
                else:
                    failed.append(next_test)
            except:
                failed.append(next_test)
    
    return passed, failed

def report(passed, failed, outfile=None, quiet=False):
    possible = 0
    earned = 0
    
    def summarize(description, cases):
        if len(cases) == 0:
            return f'No cases {description.lower()}.'
        
        summary = [f'The following test cases {description}:']
        for i, c in enumerate(cases):
            summary.append(f"{i+1}. Command: {c['cmd'][2:]}")
            summary.append(f"\t Observed output: {c['response']}")
            summary.append(f"\t Expected output: {c['target']}")
            summary.append(f"\t Points: {c['points']}")
            summary.append('')
    
        return '\n'.join(summary[:-1])
    
    for p in passed:
        earned += p['points']
        possible += p['points']
    
    for f in failed:
        possible += f['points']
    
    if outfile is None:
        dest = sys.stdout
    else:
        dest = open(outfile, 'w+')
    
    if (outfile is not None) or (not quiet):
        print(f'Total points earned: {np.round(earned, decimals=2)}/{np.round(possible, decimals=2)} = {np.round(100 * np.round(float(earned), decimals=4)/np.round(float(possible), decimals=4), decimals=2)}%', file=dest)
        print('\nDetails:\n', file=dest)
        print(summarize('PASSED', passed), file=dest)
        print('\n', file=dest)
        print(summarize('FAILED', failed), file=dest)
    
    if outfile is not None:
        dest.close()
    
    return np.round(100.0 * float(earned) / float(possible), decimals=2)

def grade_assignment(submission, rubrics, outfile=None, quiet=False):
    passed, failed = grade(submission, rubrics)
    return report(passed, failed, outfile=outfile, quiet=quiet)
