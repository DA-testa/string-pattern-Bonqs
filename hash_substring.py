def read_input():
    inp = input()
    if inp[0] == 'F':
        with open('./tests/06', 'r') as f:
            pattern, text = map(str.strip, f.readlines())
    elif inp[0] == 'I':
        pattern = input().strip()
        text = input().strip()
    return pattern, text
def print_occurrences(output):
    print(*output)
def get_occurrences(pattern, text):
    occurrences = [i for i in range(len(text) - len(pattern) + 1) if text[i:i+len(pattern)] == pattern]
    return occurrences
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
