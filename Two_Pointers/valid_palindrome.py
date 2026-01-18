#Valid Palindrome
#Return True if strin is Palindrome(ignore non alpha-numeric characers and case)

def is_palindrome(s):
    s = s.lower( ) #convert to lowercase

    left = 0
    right = len(s)-1

    while left < right:
        #move left pointer to next alphanumeric
        while left < right and not s[left].isalnum():
            left +=1

        #move right pointer to previous alphanumeric
        while left < right and not s[right].isalnum():
            right -=1
        
        #compare characters
        if s[left] != s[right]:
            return False
        
        left += 1
        right -=1

    return True

if __name__ == "__main__":
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"

    print("Input:", s1)
    print("Output:", is_palindrome(s1))  # True

    print("Input:", s2)
    print("Output:", is_palindrome(s2))  # False
     
