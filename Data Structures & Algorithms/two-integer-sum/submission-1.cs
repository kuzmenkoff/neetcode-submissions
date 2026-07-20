public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> d = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++){
            if (!d.ContainsKey(target - nums[i])){
                d[nums[i]] = i;
            }
            else {
                return new int[] { d[target - nums[i]], i };
            }
        }
        return new int[] {0, 1};
    }
}
