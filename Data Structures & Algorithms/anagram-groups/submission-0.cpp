class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> mp;
        for (auto it : strs) {
            string k = it;
            sort(k.begin(), k.end());
            mp[k].push_back(it);
        }
        vector<vector<string>> ans;
        for (auto it : mp) {
            vector<string> temp;
            for (auto i : it.second) {
                temp.push_back(i);
            }
            ans.push_back(temp);
        }
        return ans;
    }
};