'''
    풀이 시간: 미해결
    
    왼쪽/오른쪽 부분을 나눠서 왼쪽의 최댓값, 오른쪽의 최댓값을 구하고
    왼쪽 부분의 물이 고이는 양: 왼쪽 최댓값 - 현재 왼쪽 인덱스의 값
    오른쪽 부분의 물이 고이는 양: 오른쪽 최댓값 - 현재 오른쪽 인덱스의 값
    이 두 값을 더해서 물이 고이는 전체 양을 구한다...

    느낀점: 왼쪽/오른쪽 최댓값을 구해야 한다는 건 알았는데, 인덱스를 조정하는 부분이 생각하기 어려웠다
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        region_count = 0
        
        left, right = 0, len(height)-1
        max_left = height[left]
        max_right = height[right]

        # 투포인터를 이용해 왼쪽, 오른쪽의 물이 고이는 부분을 구함
        while left < right:
            # 왼쪽/오른쪽 부분의 최댓값을 찾음
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])

            if max_left <= max_right:        # 오른쪽 부분의 최댓값이 더 크면, 오른쪽으로 이동
                region_count += max_left - height[left]
                left += 1
            else:                            # 왼쪽 부분의 최댓값이 더 크면, 왼쪽으로 이동
                region_count += max_right - height[right]
                right -= 1

        return region_count