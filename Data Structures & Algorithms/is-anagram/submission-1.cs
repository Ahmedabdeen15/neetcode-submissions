public class Solution {
    public bool IsAnagram(string s, string t)
    {
        if (s.Length != t.Length) return false;
        var FrequencyCount = new int[26];
        for (int i = 0; i < s.Length; i++)
        {
            FrequencyCount[s[i] - 'a']++;
            FrequencyCount[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; i++)
        {
            if (FrequencyCount[i] != 0)
            {
                return false;
            }
        }
        return true;
    }
}
