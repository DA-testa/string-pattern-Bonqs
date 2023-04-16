def r(): return(input().strip(), input().strip()) if input().startswith('T') else (open('./tests/06').read().splitlines())
l = print
g = lambda x, t: [i for i in range(len(t) - len(x) + 1) if t[i:i+len(x)] == x]
if __name__=='__main__': l(g(*r()))
