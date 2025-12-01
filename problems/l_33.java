class Solution {
    public int search(int[] nums, int target) {
        if(nums.length==1&&nums[0]==target) return 0;
        int lidx = 0;
        int ridx = nums.length-1;
        while(lidx<ridx){
            int fidx = lidx+(ridx-lidx)/2;
            if(target==nums[lidx]) return lidx;
            if(target==nums[ridx]) return ridx;
            if(ridx-lidx==1) break;
            if(nums[lidx]<nums[ridx]){
                if(nums[fidx]>target){
                    ridx = fidx;
                }else{
                    lidx = fidx;
                }
            }else{//lidx>ridx
                if(nums[ridx]>=target){
                    if(nums[ridx]>nums[fidx]){
                        if(nums[fidx]>target){
                            ridx = fidx;
                        }else{
                            lidx = fidx;
                        }
                    }else{
                        lidx = fidx;
                    }
                }else{ //lidx<=target
                    if(nums[lidx]<nums[fidx]){
                        if(nums[fidx]<target){
                            lidx = fidx;
                        }else{
                            ridx = fidx;
                        }
                    }else{
                        ridx = fidx;
                    }
                }
            }
        }
        return -1;
    }
}