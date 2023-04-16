def r(): return input().strip(), input().strip() if input()[0] != 'F' else map(str.strip, open('./tests/06').readlines())
def l(o): print(*o)
def g(x,t): return [i for i in range(len(t)-len(x)+1) if t[i:i+len(x)] == x]
if __name__ == '__main__': l(g(*r()))
