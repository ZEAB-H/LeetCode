class Solution:
    # this is how it works, 
    # first we will create an empty array and add fields in thre , and we keep adding to it
    # and each time wjhile we add we will check if the next number is part of the new set , and 
    #and if we get it in there we will return true , other wise we will make it false after adding to it 
    
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
