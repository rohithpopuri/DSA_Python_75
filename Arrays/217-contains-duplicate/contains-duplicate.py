class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        has = set()
        for i in nums :
            if i in has :
                return True
            has.add(i)
        return False 

        