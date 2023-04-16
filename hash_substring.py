def r():
 p=input();x,t=(input if p[0]!='F' else lambda:open('./tests/06')).strip().readlines();return x.strip(),t.strip()
l=lambda o:print(*o)
g=lambda x,t:[i for i in range(len(t)-len(x)+1)if t[i:i+len(x)]==x]
if __name__=='__main__':l(g(*r()))
