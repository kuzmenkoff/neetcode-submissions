public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary <char, int> d1 = new Dictionary <char, int> ();
        Dictionary <char, int> d2 = new Dictionary <char, int> ();
        for (int i = 0; i < s.Length; i++){
            if (!d1.ContainsKey(s[i]))
                d1[s[i]] = 1;
            else {
                d1[s[i]]++;
            }
        }

        for (int i = 0; i < t.Length; i++){
            if (!d2.ContainsKey(t[i]))
                d2[t[i]] = 1;
            else {
                d2[t[i]]++;
            }
        }

        if (d1.Count != d2.Count) return false;
        else{
            foreach (var kvp in d1)
                if (!d2.TryGetValue(kvp.Key, out int v) || v != kvp.Value) return false;
            return true;
        }
    }
}
