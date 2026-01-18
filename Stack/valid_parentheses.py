#Valid Parentheses
#Reurn True if the input string has valid parentheses, otherwise return False.

def is_valid_parentheses(s):
    stack = [] #stack will store opening brackets

    #mapping of closing brackets to opening brackets
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        #if ch is a closing bracket
        if ch in mapping:
            #take the last opening bracket from stack(if stack is not empty)
            top = stack.pop() if stack else '#'

            #if the last opening bracket does not match
            if mapping [ch] !=top:
                return False
        else:
            #opening bracket, push into sack
            stack.append(ch)

    #if stack becomes empty at the end ==> valid parentheses
    return len(stack) ==0


if __name__ == "__main__":
   print(is_valid_parentheses("()"))          # True
   print(is_valid_parentheses("()[]{}"))      # True    
   print(is_valid_parentheses("(]"))          # False
   print(is_valid_parentheses("([)]"))        # False
   print(is_valid_parentheses("{[]}"))        # True 
