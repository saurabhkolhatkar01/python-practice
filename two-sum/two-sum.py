class TwoSum:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = list()
        for index in range(len(nums)):
            int_x = target - nums[index];
            int_y = self.findIndex(int_x, index, nums)
            if int_y is not None:
                result.append(int_y)

        result.sort()
        print(result)

    def findIndex(self, x: int, index: int, nums: list[int]):
        for i in range(len(nums)):
            if i != index and x == nums[i]:
                return i



arr_nums = [int(x) for x in list(input("Enter the list items space separated:").strip(" ").split(" "))]
int_target = int(input("Enter Target:"))
obj_two_sum = TwoSum()
obj_two_sum.twoSum(arr_nums, int_target)