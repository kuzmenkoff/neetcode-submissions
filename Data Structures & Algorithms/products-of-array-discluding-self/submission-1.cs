public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
       int prefix = 1;
       int suffix = 1;
       int n = nums.Length;
       int[] result = new int[n];
       Array.Fill(result, 1);
       for (int i = 0; i < n; i++){
            result[i] = prefix;
            prefix *= nums[i];
        }

        for (int i = n - 1; i >= 0; i--){
            result[i] *= suffix;
            suffix *= nums[i];
        }

        return result;
    }
}
