class Solution:
    def trap(self, height: List[int]) -> int:
        maxW = 0 

        l,r = (0,len(height)-1)
        leftMax,rightMax =height[l],height[r]
        while l < r: 
            if height[l] < height[r]: 
                l+=1
                leftMax = max(height[l],leftMax)
                if height[l] < leftMax: 

                    maxW += leftMax - height[l]
            else:

                r-=1
                rightMax = max(height[r],rightMax) 
                if height[r] < rightMax: 
                    maxW += rightMax - height[r]

        return maxW    