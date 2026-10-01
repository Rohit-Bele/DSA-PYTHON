def leftRightDifference(nums):
        left_sum = [0] * len(nums)
        right_sum = [0] * len(nums)
        ans = [0] * len(nums)

        for i in range(1,len(nums)):
            left_sum[i]=nums[i-1]+left_sum[i-1]
        
        for j in range(len(nums)-2,-1,-1):
            right_sum[j]=nums[j+1]+right_sum[j+1]


        print(left_sum)
        print("**********************")
        print(right_sum)

list1 = [10,4,8,3]

leftRightDifference(list1)