class Solution:
    def maxArea(self, height: list) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            w = right - left
            if height[left] <= height[right]:
                area = max(area, w * height[left])
                left += 1
            else:
                area = max(area, w * height[right])
                right -= 1
        return area

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))