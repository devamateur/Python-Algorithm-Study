'''
    배열에서 서로 다른 세 수의 합이 0이 되는 수들의 인덱스 구하기
    풀이 시간: 미해결
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]: continue         # 같은 값 스킵
            target = -nums[i]

            j, k = i+1, len(nums)-1        # 투포인터

            while j < k:
                if nums[j] + nums[k] == target:        # a+b+c = 0 -> b+c = -a
                    result.append([nums[i], nums[j], nums[k]])

                    ##### 같은 값 스킵
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                else:
                    if nums[j] + nums[k] < target:
                        j += 1
                    else:
                        k -= 1
        return result