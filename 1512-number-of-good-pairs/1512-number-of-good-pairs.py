class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs= 0
        d={}
        for num in nums:
            if num not in d :
                d[num]=1
            else:
                d[num] +=1
                good_pairs += d[num]-1
            
        return good_pairs
#         for i in range(len(nums)):
#             j=i+1
#             for j in range(len(nums)):
#                      if nums[i]== nums[j]:
#                         good_pairs+=1
#                         j+=1
                        
                    
                    
                
   