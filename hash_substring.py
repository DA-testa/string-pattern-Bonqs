def r():
    p = input()
    if p[0] == 'F':
        with open('./tests/06') as f: x,t=map(str.strip,f.readlines())
    else: x,t=input().strip(),input().strip()
    return x,t
def l(o): print(*o)
def g(x,t): return[i for i in range(len(t)-len(x)+1)if t[i:i+len(x)]==x]
if __name__=='__main__': l(g(*r()))
