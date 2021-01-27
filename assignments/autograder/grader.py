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
from configparser import ConfigParser
import plotly.express as px
from string import ascii_lowercase
import itertools

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


def get_fname_suffix(n):
    '''
    return a list of suffixes to append to fnames with the same base:
    a, b, c, ..., z, aa, ab, ..., az, ba, ..., bz, aaa, aab, ...
    '''
    #source: https://stackoverflow.com/questions/29351492/how-to-make-a-continuous-alphabetic-list-python-from-a-z-then-from-aa-ab-ac-e/29351603    
    def generate_id():
        i = 1
        while True:
            for s in itertools.product(ascii_lowercase, repeat=i):
                yield ''.join(s)
            i += 1
    
    gen = generate_id()
    
    def helper():
        for s in gen:
            return s
    
    return [helper() for i in range(n)][-1]



def extract_assignment(dir):
    pattern = r'([a-z\-]+)-((([0-9]{2,4})-){5}[0-9]{2,4})'
    assignment = re.findall(pattern, os.path.split(dir)[1])[0][0]
    return assignment.lower()

def get_students(submissions_dir):
    contents = [os.path.split(g)[1] for g in glob(os.path.join(submissions_dir, '*'))]
    return [c for c in contents if os.path.isdir(os.path.join(submissions_dir, c))]

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
            r.at[i, 'args'] = eval(f"{r.loc[i]['args']}")
            
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

def commit_and_push(submissions_dir, students, root=None, private_dir=None, debug=True):
    feedback_branch = 'feedback'
    assignment = extract_assignment(submissions_dir)
    
    if root is None:
        root = os.path.abspath(os.path.join('..', '..', '..'))
    if private_dir is None:
        private_dir = os.path.join(root, 'teaching-tools', 'cs-for-psych', 'assignments')
    
    #set up git
    gitconfig = ConfigParser()
    gitconfig.read(os.path.join(private_dir, 'autograder', 'git.ini'))

    os.system(f"git config --global user.name '{gitconfig['github']['user.name']}'");
    os.system(f"git config --global user.email '{gitconfig['github']['user.email']}'");
    
    def commit_and_push_single_student(s, debug=True):
        mydir = os.path.join(submissions_dir, s)
        os.chdir(mydir)
        
        if debug:
            token = '<TOKEN>'
        else:
            token = gitconfig['github']['token']
        
        cmds = [f"git remote add {s} https://{token}@github.com/ContextLab/{assignment}-{s}.git", #f'git pull {s} {feedback_branch}', #comment this out after pushing revised reports
                f'git fetch {s}',
                f'git checkout -b {feedback_branch}',
                'git add report.txt', 
                'git commit -a -m "added autograder report"',
                f'git push {s} HEAD:{feedback_branch}']
        if debug:
            print(f'Simulating commands (running from directory: {mydir})')
            [print('\t' + c) for c in cmds]
            print('\n')
        else:
            [os.system(c) for c in cmds]
    
    start_dir = os.getcwd()
    [commit_and_push_single_student(s, debug=debug) for s in students]
    os.chdir(start_dir)

def autograde(submissions_dir, root=None, plot_it=False, grading_repo=None, public_checks_dir=None, private_checks_dir=None):    
    if root is None:
        root = os.path.abspath(os.path.join('..', '..', '..'))
    if grading_repo is None:
        grading_repo = os.path.join(root, 'cs-for-psych', 'assignments', 'autograder')
    if public_checks_dir is None:
        public_checks_dir = os.path.join(root, 'cs-for-psych', 'assignments')
    if private_checks_dir is None:
        private_checks_dir = os.path.join(root, 'teaching-tools', 'cs-for-psych', 'assignments')
    
    #set up git
    gitconfig = ConfigParser()
    gitconfig.read(os.path.join(private_checks_dir, 'autograder', 'git.ini'))

    os.system(f"git config --global user.name '{gitconfig['github']['user.name']}'");
    os.system(f"git config --global user.email '{gitconfig['github']['user.email']}'");
    
    #get assignment and rubrics
    assignment = extract_assignment(submissions_dir)
    public_rubric = os.path.join(public_checks_dir, assignment, 'public_rubric.xls')
    private_rubric = os.path.join(private_checks_dir, assignment, 'private_rubric.xls')
    rubrics = [public_rubric, private_rubric]
    
    #autograde all students
    students = get_students(submissions_dir)
    grades = [autograde_notebooks(submissions_dir, rubrics, s) for s in students]
    grades = pd.DataFrame(zip(students, grades), columns=['Student', 'Score']).set_index('Student')
    
    fig = px.histogram(grades, x='Score', range_x=[0, 100], nbins=10, histnorm='percent');
    fig.update_layout(yaxis_title='Percentage of students');
    fig.write_image(os.path.join(submissions_dir, 'grade_summary.pdf'));
    
    return grades

def autograde_notebooks(submissions_dir, rubrics, student):  
    def grade_notebook(notebook_fname, outfile=None, quiet=False):        
        basedir, notebook = os.path.split(notebook_fname)
        target = notebook[:-6]

        bad_chars = [' ', '-', ',', '!', '?', '.']
        modified_target = target

        for b in bad_chars:
            if b in modified_target:
                modified_target = modified_target.replace(b, '_')

        print(f'grading: {target}.ipynb')
        clean_up = False
        if modified_target != target:
            if os.path.exists(os.path.join(basedir, modified_target + '.ipynb')):
                clean_up = True
                os.rename(os.path.join(basedir, modified_target + '.ipynb'), os.path.join(basedir, modified_target + '.ipynb.BACKUP'))
            os.rename(os.path.join(basedir, target + '.ipynb'), os.path.join(basedir, modified_target + '.ipynb'))

        #mydir = os.getcwd()
        if 'submission' in sys.modules:
            print('pop!')
            sys.modules.pop('submission')
        try:        
            os.chdir(basedir)
            submission = notebook_to_module(modified_target)
            score = grade_assignment(submission, rubrics, quiet=quiet, outfile=outfile)
        except:
            print('** ERROR!')
            if outfile is not None:
                with open(outfile, 'w') as fd:
                    print('Assignment could not be autograded: notebook failed to run!', file=fd)
            score = 0.0
        #os.chdir(mydir)

        if modified_target != target:
            os.rename(os.path.join(basedir, modified_target + '.ipynb'), os.path.join(basedir, target + '.ipynb'))

        if clean_up:
            os.rename(os.path.join(basedir, modified_target + '.ipynb.BACKUP'), os.path.join(basedir, modified_target + '.ipynb'))

        return score
    
    start_dir = os.getcwd()    
    mydir = os.path.join(submissions_dir, student)
    
    os.chdir(mydir)
    notebooks = glob(os.path.join('.', '*.ipynb'))
    grades = [grade_notebook(n, quiet=True) for n in notebooks]
    
    best_notebook = notebooks[np.where(np.array(grades) == np.max(grades))[0][0]]
    best_grade = grade_notebook(best_notebook, quiet=True, outfile='report.txt')    
    os.chdir(start_dir)
    return best_grade