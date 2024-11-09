'''
    2n개 원소가 있는 정수 리스트가 주어질 때,
    각 원소들을 2개씩 페어링해서 (a1, b1), (a2, b2), ..., (an, bn)
    min(ai, bi)값이 최대가 될 때의 합을 구하는 문제

    풀이 시간: 5분
'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # min()끼리 합한게 최대가 되려면, 작은값은 작은값끼리 큰값은 큰값끼리 페어링 해야 함

        result = 0
        nums.sort()
        
        # 페어링한 값에서 min()은 짝수번 인덱스
        for i in range(0, len(nums), 2):
            result += nums[i]
        
        return result