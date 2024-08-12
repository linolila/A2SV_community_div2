class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        temp = 0
        for i in range(len(nums)):
            fast = slow = i 
            x=i
            cont=False

            while x < len(nums) and x>=0:
                if nums[i]>=0:
                    if nums[x]<0:
                        cont=True
                        break
                else:
                    if nums[x]>0:
                        cont=True
                        break
                x+=nums[x]
           
            if cont:
                continue

            while True:

                slow = (slow + nums[slow]) % len(nums)
                
                fast = (fast + nums[fast]) % len(nums)
                
                temp = nums[fast]

                fast = (fast + nums[fast]) % len(nums)
            
                if slow == fast:
                    break
                if nums[i] * nums[slow] <= 0 or nums[i] * nums[fast] <= 0:
                    break
                if slow == (slow + nums[slow]) % len(nums):
                    break
            if slow == fast and slow != (slow + nums[slow]) % len(nums):
                    return True

        return False
