#Single Number(LeetCode 136)
#Every element appears twice except for one. Find that one

def single_number(nums):
    ans = 0

    for num in nums:
        ans ^= num #XOR cancels duplicates
    return ans

if __name__ == "__main__":
    nums = [4,1,2,1,2]
    print("Input:", nums)
    print("Output:", single_number(nums)) # 4