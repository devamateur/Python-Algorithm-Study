'''
    정수 배열에서 현재 인덱스 원소를 제외한 나머지 원소들의 곱 구하기

    풀이 시간: 45분

    1. 모든 원소를 곱하고 현재 인덱스 원소로 나누자 -> 나누기 연산자 사용 불가여서 패스
    2. 현재 인덱스의 원쪽 원소들의 곱, 오른쪽 원소들의 곱을 구해 곱하기
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 나누기 연산자를 사용하지 않는 O(N) 코드 작성

        p = [1]*len(nums)           # 왼쪽 부분 곱
        p2 = [1]*len(nums)          # 오른쪽 부분 곱

        for i in range(1, len(nums)):
            p[i] = p[i-1] * nums[i-1]           # p[i-1]: nums[i-1]을 제외한 이전 원소들(왼쪽) 곱

        for i in range(len(nums)-2, -1, -1):
            p2[i] = p2[i+1] * nums[i+1]         # p2[i+1]: nums[i+1]을 제외한 이전 원소들(오른쪽) 곱
        
        # 두 리스트를 곱하면 현재 원소를 제외한 모든 원소들 곱이 나옴
        for i in range(len(nums)):
            p[i] = p[i]*p2[i]
        return p

# 정답 코드
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out