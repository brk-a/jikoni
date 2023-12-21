'''
there is a string of four letters: A, B, C and D
the string can be transformed in one of two ways:
    1. remove A and the adjacent B
    2. remove C and the adjacent D
write a function, def solution(S), that returns a string
said string is one of the following:
    1. string obtained from S by repeatedly applying said transformations
    2. string cannot be further transformed
if there is more than one way to apply the transformations, choose any valid one
'''

def solution(S):
    changed = True
    
    while changed:
        changed = False
        i = 0
        while i < len(S) - 1:
            if (S[i] == 'A' and S[i+1] == 'B') or (S[i] == 'B' and S[i+1] == 'A'):
                S = S[:i] + S[i+2:]
                changed = True
            elif (S[i] == 'C' and S[i+1] == 'D') or (S[i] == 'D' and S[i+1] == 'C'):
                S = S[:i] + S[i+2:]
                changed = True
            i += 1
    
    return S