class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0 
        trap = 0

        l,r= (0,len(height)-1)
        maxLeft, maxRight = (height[l],height[r])
        while(l < r): 
            if height[l] < height[r]: 
                l+=1
                maxLeft = max(height[l],maxLeft)
                if height[l] < maxLeft: 
                    trap += maxLeft -height[l]
            else:
                r-=1
                maxRight = max(height[r],maxRight)
                if height[r] < maxRight:
                    trap += maxRight - height[r]
        
        return trap

