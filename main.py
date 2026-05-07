import os        # F401: imported but unused
import sys       # F401: another unused import

x=1+1            # E225: missing whitespace around operator

def foo():
    y = 1
    return       # F821 / general: defined but never used (y)

l = 1            # E741: ambiguous variable name 'l'
