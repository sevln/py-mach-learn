import sys

def fix(file):
    output = open(file[1] + 'fixed.pkl', 'w', newline='\n')
    output.write(open(file[1], 'r').read())