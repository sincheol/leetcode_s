class Solution {
    int max = Integer.MIN_VALUE;
    public int maxProduct(int[] nums) {
        if(nums.length==0)return max;
        if(nums.length==1)return nums[0];
        int cntm = 0;
        int cntz = 0;
        int[] midx = new int[nums.length];
        int[] zidx = new int[nums.length];
        for(int i = 0; i<nums.length; i++){
            if(nums[i]<0) midx[cntm++] = i;
            if(nums[i]==0) zidx[cntz++] = i;
            if(max<nums[i]) max = nums[i];
        }
        if(cntz==0){
            if(cntm%2==0) return cal(0,nums.length,nums);
            return Math.max(cal(0, midx[cntm-1], nums), cal(midx[0]+1, nums.length, nums));
        }else{
            int prev = 0;
            int cnt = 0;
            while(cnt<cntz){
                int res = maxProduct(Arrays.copyOfRange(nums,prev,zidx[cnt]));
                if(res>max){
                    max = res;
                }
                prev = zidx[cnt++]+1;
            }
            int res = maxProduct(Arrays.copyOfRange(nums,prev,nums.length));
            if(res>max){
                max = res;
            }
        }
        return max;
    }
    public int cal(int s, int e, int[]nums){
        if(s==e) return Integer.MIN_VALUE;
        int tmp = s;
        int res = nums[tmp++];
        while(tmp<e){
            res*=nums[tmp++];
        }
        return res;
    }
}
/*
longer -> larger
x0 ->   even negative -> product all
        odd negative(n) -> 0~n-2 / 1~n-1
0 ->    cut and recursion to x0
- count -> if even keep but odd skip
*/