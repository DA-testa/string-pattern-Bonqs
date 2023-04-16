def find_occurrences():
    text = input().strip().split()
    pattern = text[0]
    string = text[1]
    return [i for i in range(len(string)-len(pattern)+1) if string[i:i+len(pattern)] == pattern]
if __name__ == '__main__':
    print(*find_occurrences())
