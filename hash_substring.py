def g():return input().rstrip(), input().rstrip(), input().rstrip() if input_choice == 'I' else open("tests/06").read().splitlines()
def f(o):print(*o)
def h(p,t):l,m,n,o=len(p),len(t),hash(p),hash(t[:l]),[];[o.append(i) for i in range(n-l+1)if m-i>=l==o and p==t[i:i+l]or(o,o_hash)=(o,hash(t[i+1:i+l+1]))if i<m-l];return o
if __name__=='__main__':f(h(*g()))
