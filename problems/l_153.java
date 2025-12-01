class Solution {
    int min = Integer.MAX_VALUE;
    public int findMin(int[] nums) {

        if(nums.length==1) return nums[0];
        int l2 = nums.length/2;
        if(nums[0]<nums[l2]) {
            int tmp = Math.min(nums[0],findMin(Arrays.copyOfRange(nums, l2, nums.length)));
            if(tmp<min) min = tmp;
        }else{
            int tmp = Math.min(nums[l2],findMin(Arrays.copyOfRange(nums, 0, l2)));
            if(tmp<min) min = tmp;
        }

        return min;
    }
}
/*numslength<numslength/2+1 */