class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        op = list()

        for i in nums:
            if i in seen:
                op.append(i)
            else:
                seen.add(i)
              
        return op
