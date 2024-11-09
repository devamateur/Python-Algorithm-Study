'''
    리스트에서 합이 target이 되는 두 수의 인덱스 리턴
    풀이 시간: 20분
    중복을 제외하는 부분에서 조금 오래 걸렸다
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            x = target - nums[i]

            if x in nums[i+1:]:          # 같은 인덱스 숫자를 더하지 않기 위해 nums[i+1:]부터 확인
                return [i, nums[i+1:].index(x)+i+1]         # 슬라이싱한 인덱스만큼 더해서 원래 인덱스 복구