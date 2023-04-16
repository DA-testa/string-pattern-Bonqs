def read_input():
    p = input()
    if p[0] == 'F':
        with open('./tests/06', 'r') as f:
            x, y = map(str.strip, f.readlines())
    elif i[0] == 'I':
        x = input().strip()
        y = input().strip()
    return x, y
def g(x, y):
    o = [i for i in range(len(y) - len(x) + 1) if y[i:i+len(x)] == x]
    return o
if __name__ == '__main__':
    print(*g(*read_input()))
