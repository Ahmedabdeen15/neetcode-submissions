public class Solution {
        public bool IsAnagram(string s, string t)
    {
        if (s.Length != t.Length) return false;
        var FrequencyCount = new Dictionary<char, int>();
        foreach (char x in s)
        {
            if (FrequencyCount.ContainsKey(x))
            {
                FrequencyCount[x]++;
            }
            else
            {
                FrequencyCount[x] = 1;
            }
        }
        foreach (char x in t)
        {
            if (FrequencyCount.ContainsKey(x))
            {
                FrequencyCount[x]--;
            }
            else
            {
                return false;
            }
        }
        foreach (var item in FrequencyCount)
        {
            if (item.Value != 0)
            {
                return false;
            }
        }
        return true;
    }
}
