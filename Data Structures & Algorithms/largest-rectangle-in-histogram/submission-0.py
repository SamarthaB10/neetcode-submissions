class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        maxArea = 0 
        for i in range(len(heights)): 
            while stack and heights[i] < heights[stack[-1]]: 
                height = heights[stack.pop()]

                width = i if not stack else i - stack[-1] -1
                curArea = height* width 

                maxArea = max(maxArea,curArea) 
            

            stack.append(i)
        return maxArea


'''
maxArea = []
for h in heights:

'''