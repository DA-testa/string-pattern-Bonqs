def r():return(input().strip(),input().strip())if input().startswith('F'):with open('./tests/06') as f: x,t=map(str.strip,f.readlines())else(input().strip(),input().strip())
def l(o):print(*o)
def g(x,t):return[i for i in range(len(t)-len(x)+1)if t[i:i+len(x)]==x]
if __name__=='__main__':l(g(*r()))
