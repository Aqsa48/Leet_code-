# solution 1.

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arrEven=[]
        arrOdd=[]
        for x in nums:
            if x% 2 ==0:
                arrEven.append(x)
            else:
                arrOdd.append(x)
        return arrEven+arrOdd
# solution 2
