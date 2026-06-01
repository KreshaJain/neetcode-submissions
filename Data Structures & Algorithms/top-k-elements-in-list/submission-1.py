class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        ans = []

        
        for i in range(k):

            maxi = 0
            element = 0

           
            for key in d:

                if d[key] > maxi:
                    maxi = d[key]
                    element = key

            ans.append(element)

            
            d[element] = -1

        return ans     