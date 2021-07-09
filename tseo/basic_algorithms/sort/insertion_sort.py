from typing import List


def insertion_sort(nums: List[int], asc=True) -> List[int]:
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):  # range(시작인덱스, 종료인덱스, step)
            if asc:  # 오름차순
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
            else:  # 내림차순
                if nums[j - 1] < nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]


if __name__ == "__main__":
    n = [3, 1, 4, 5, 1, 2, 3, 4, 5, 6]
    print(n)
    insertion_sort(n)
    print(n)
    insertion_sort(n, asc=False)
    print(n)

