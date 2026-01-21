#Longest Substring without reapeating characters (LeetCode3)
#Return Length of longest substring without repeating chahracters

def length_of_longest_substring(s):
    seen = {}  #char --> last index
    left = 0   #start of window
    best = 0

    for right, ch in enumerate(s):
        #if character is already seen and inside current window
        if ch in seen and seen[ch] >=left:
            left = seen[ch] + 1 #move left pointer

        seen[ch] = right #update last seen index
        best = max(best, right - left + 1)

    return best

if __name__ == "__main__":
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"

    print("Input:", s1, "Output:", length_of_longest_substring(s1))  # 3
    print("Input:", s2, "Output:", length_of_longest_substring(s2))  # 1
    print("Input:", s3, "Output:", length_of_longest_substring(s3))  # 3 




    