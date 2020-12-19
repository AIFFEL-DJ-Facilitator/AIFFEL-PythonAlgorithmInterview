#input = ()[]{}
#output = True

def isValid(s):
    stack = []
    talbe = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
    }

    for char in s:
        if char not in table: # '('
            stack.append(char) # stack = ['(']
        elif not stack or table[char] != stack.pop(): #')' table에 있고 '(' == '(' (pop된 상태)
            return False
    return len(stack) == 0