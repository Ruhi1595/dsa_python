#Valid Anagram(leetcode)
#Return True if t is an anagram of s

def is_anagram(s,t):
    #if lengths diifer, they cant be anagrams
    if len(s)!= len(t):
        return False
    
    freq = { } #char--> count
     # count letters in s
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    #count characters in s
    for ch in s:
        if ch not in freq:
            return False #character in t is not found in s
        
        freq[ch] -=1

        if freq[ch] ==0:
            del freq[ch] #keeps the dict clean (optional)

    #if everything matched, freq should be empty
    return len(freq) == 0
if __name__ == "__main__":
    s1, t1 = "anagram", "nagaram"
    s2, t2 = "rat", "car"

    print("Input:", s1, t1)
    print("Output:", is_anagram(s1, t1))  # True

    print("Input:", s2, t2)
    print("Output:", is_anagram(s2, t2))  # False




