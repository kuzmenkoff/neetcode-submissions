public class Solution {
    public int LongestConsecutive(int[] nums) {
        HashSet<int> d = new HashSet<int>();
        foreach (int num in nums)
            d.Add(num);
        int longest = 0;
            
        foreach (int num in nums)
            if (!d.Contains(num - 1)) {
                int length = 0;
                while (d.Contains(num + length))
                    length++;
                longest = Math.Max(longest, length);
            }
        return longest;
    }
}
