# Contains Duplicate (leetcode)
# Returns True if any value appears atleast twice

def contains_duplicate (nums):
    seen = set() #empty set to sore visied numbers

    for num in nums:

        if num in seen:
           return True
    
    
    
       #otherwise add number to set
        seen.add(num)

    #if loop finishes, no duplicates
    return False

if __name__ == '__main__':
     nums1 = [1,2,3,1]
     nums2 = [1,2,3,4]

     print("Input:",nums1)
     print("Output:",contains_duplicate(nums1)) #True

     print("Input:",nums2)
     print("Output:",contains_duplicate(nums2)) #False





