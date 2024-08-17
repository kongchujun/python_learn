
from typing import List
def find_max_avg(nums: List[int], k: int) -> float:
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum + nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum/k

if __name__ == '__main__':
    nums1 = [1, 12, -5, -6, 50, 3]
    print(find_max_avg(nums1, 4))