def read_input():
    p = input()
    if p[0] == 'F':
        with open('./tests/06', 'r') as f:
            x, t = map(str.strip, f.readlines())
    elif p[0] == 'I':
        x = input().strip()
        t = input().strip()
    return x, t
def l(o):
    print(*o)
def g(x, t):
    c = [i for i in range(len(t) - len(x) + 1) if t[i:i+len(x)] == x]
    return c
if __name__ == '__main__':
    l(g(*read_input()))
