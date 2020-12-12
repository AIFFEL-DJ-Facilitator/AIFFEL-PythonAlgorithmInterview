# sample = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]


def solution(s):
    letters, digits = [], []
    for log in s:
        if log.split()[1].isdigit(): # ['8', 'art', '3', 'own', 'art']
            digits.append(log) # ['dig1 8 1 5 1' ,'dig2 3 6']
        else:
            letters.append(log) #['let1 art can', 'let2 own kit dig', 'let3 art zero']

    letters.sort(key = lambda x: (x.split()[1:], x.split()[0])) # ['let1 art can', 'let3 art zero', 'let2 own kit dig']
    return letters + digits # ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']