def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nlist = []
    x = 0
    y = x+1
    z = len(nums)
    while x < z:
        while y < z and x != y:
            sum = nums[x] + nums[y]
            
            print nums[x],nums[y],sum
            if(sum == target):
                nlist.append(x)
                nlist.append(y)
                return nlist 
            else:
                y+=1
        x+=1
        y = x+1
    return nlist

def main():
    nums = [3,2,4]
    target = 6
    sol = twoSum(nums,target)
    print sol
    #nums = [3,2,4]
    #target = 6
    #twoSum(nums,target)


if __name__ == '__main__':
    main()