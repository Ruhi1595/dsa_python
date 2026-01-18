print("Hello Ruhi! VS code is working")

#Two sum Leetcode
#Return indices of two numbers which adds up to target
def two_sum_bruteforce(nums, target):
    """
    Bruteforce solution (O(n^2))
    Try every pair of numbers
    """
    n = len(nums)
    
    for i in range (n):
        for j in range(i+1,n):
            if nums[i]+nums[j]== target:
                return[i,j]
            
    
def two_sum_hashmap(nums, target):
    """
    Optimised solution using HashMap/Dictionary(O(n))

    """
    seen = {} #number-->index
    for i, num in enumerate(nums):
        need = target - num

        if need in seen:
            return[seen[need],i]
        
        seen[num] = i

if __name__=='__main__':
    #Test Case
    nums = [2,7,11,15]
    target = 9

    print("Nums:",nums)
    print("target:", target)

    print("Brute force answer:", two_sum_bruteforce(nums,target))
    print("Hashmap answer:", two_sum_hashmap(nums,target))


            
