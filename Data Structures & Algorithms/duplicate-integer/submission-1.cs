public class Solution
{
    public bool hasDuplicate(int[] nums)
    {
        HashSet<int> d = new HashSet<int>();
        foreach (int x in nums)
        {
            if (!d.Contains(x)) { d.Add(x); }
            else { return true; }
        }
        return false;
    }
}
