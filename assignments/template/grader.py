import pandas as pd
import numpy as np
import os
import ast
import sys

def convert_to_script(target):
    script_already_exists = os.path.exists(target + '.py')
    if script_already_exists:
        os.renames(target + '.py', target + '.py.BACKUP')

    os.system(f'ipython nbconvert --to python {target}.ipynb');
    
    exec(f'import {target} as submission', globals())    
    return submission, script_already_exists

def from_str(s):
    try:
        if s is np.nan:
            return ''
    except:
        pass
    
    try:
        if s is None:
            return ''
    except:
        pass
    
    try:
        if len(s) == 0:
            return ''
    except:
        pass
    
    try:
        return ast.literal_eval(s)
    except:
        return s

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
            next_test['cmd'] = f"x.{r.loc[i]['input']} == {from_str(r.loc[i]['solution'])}"
            next_test['target'] = True
        else:
            next_test['cmd'] = f"x.{r.loc[i]['function']}({str(from_str(r.loc[i]['input']))})"
            next_test['target'] = from_str(r.loc[i]['solution'])
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

def report(passed, failed, outfile=None):
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
        
    print(f'Total points earned: {earned}/{possible} = {100 * np.round(float(earned)/(float(possible)), decimals=4)}%', file=dest)
    print('\nDetails:\n', file=dest)
    print(summarize('PASSED', passed), file=dest)
    print('\n', file=dest)
    print(summarize('FAILED', failed), file=dest)
    
    if outfile is not None:
        dest.close()

def grade_assignment(submission, rubrics, outfile=None):
    passed, failed = grade(submission, rubrics)
    report(passed, failed, outfile=outfile)

def clean_up(target, script_already_exists):
    os.remove(target + '.py')
    if script_already_exists:
        os.renames(target + '.py.BACKUP', target + '.py')