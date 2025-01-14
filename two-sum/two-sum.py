class TwoSum:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Initialize an empty dictionary to store number and its index
        num_to_index = {}

        # Iterate over the list
        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num

            # Check if complement is in the dictionary
            if complement in num_to_index:
                # Return the indices of the complement and the current number
                return [num_to_index[complement], index]

            # Add the current number and its index to the dictionary
            num_to_index[num] = index

        # If no solution is found (though guaranteed to exist), return None
        return None



arr_nums = [int(x) for x in list(input("Enter the list items space separated:").strip(" ").split(" "))]
int_target = int(input("Enter Target:"))
obj_two_sum = TwoSum()
print(obj_two_sum.twoSum(arr_nums, int_target))