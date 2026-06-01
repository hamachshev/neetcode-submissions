class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1

        while left <= right:
            mid = left + (right - left) // 2
            number = nums[mid]
            print(number)
            
            if target < number: #must make it smaller
                #find non inflection side

                if nums[left] <= number: # inflection is right side
                    non_inf_low = nums[left] #leftmost is the smallest
                    if target >= non_inf_low:
                        right = mid - 1
                    else: #target is less than the lowest on the non infl side
                        #go to the right
                        left = mid + 1
                else: #inflection is left side
                    non_inf_low = nums[mid + 1]
                    if target >= non_inf_low:
                        left = mid +1
                    else: #go to infl
                        right = mid -1

            elif target > number: #make it larger
                if nums[left] < number: #inflection is right side
                    non_inf_high = nums[mid - 1]
                    if target > non_inf_high:
                        #go into inflec
                        left = mid + 1
                    else: #target is less than or eq to non inflection high
                    #go to left side
                        right = mid -1
                else: #inflection is left side
                    non_inf_high = nums[right]
                    if target > non_inf_high:
                            #go into inflec
                        right = mid -1
                    else : #target is less than non infl high
                        left = mid + 1
            else:
                return mid
        return -1