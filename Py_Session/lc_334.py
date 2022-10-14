class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        tripletA = 2147483647
        tripletB = 2147483647
        
        if (len(nums) < 3):
            return False

        for current in nums:
              
            if current > tripletB:
                return True
    
            if current <= tripletA:
                tripletA = current
            else:
                tripletB = current
                
        return  False
