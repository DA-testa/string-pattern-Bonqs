def r():p=input();x,t=map(str.strip,open('./tests/06').readlines()) if p[0]=='F' else input().strip(),input().strip();return x,t
def l(o):print(*o)
def g(x,t):return[i for i in range(len(t)-len(x)+1)if t[i:i+len(x)]==x]
if __name__=='__main__':l(g(*r()))
