class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Add a 0 to the end to force the stack to empty out at the finish line
        heights.append(0)
        stack = []
        max_area = 0
        
        for i in range(len(heights)):
            # While the stack isn't empty and the current bar is shorter 
            # than the bar represented by the top of our stack
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                
                # If stack is empty, it means this bar was the shortest seen so far,
                # so its left boundary stretches all the way to index 0 (width is just i)
                width = i if not stack else i - stack[-1] - 1
                
                max_area = max(max_area, height * width)
                
            stack.append(i)
            
        return max_area


'''
2,3,4
max

(0,1,) 
height = 7
if not stack, width = i 
2-1-1
'''