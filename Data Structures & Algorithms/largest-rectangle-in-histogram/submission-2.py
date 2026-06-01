class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxar = 0
        stack = []
        for i,h in enumerate(heights):
            s = i
            while stack and stack[-1][1]>h:
                ind,height = stack.pop()
                maxar = max(maxar,height*(i-ind))
                s= ind
            stack.append((s,h))
        for i,h in stack:
            maxar = max(maxar,h*(len(heights)-i))
        return maxar