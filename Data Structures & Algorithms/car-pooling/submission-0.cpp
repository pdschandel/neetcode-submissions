class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
      
        int n= trips.size();
        int curr = 0;
        vector<vector<int>> a;
        for(int i=0;i<n;i++){
            a.push_back({trips[i][1],trips[i][0]});
            a.push_back({trips[i][2],-trips[i][0]});
        }
        sort(a.begin(),a.end());
        for(int i=0;i<a.size();i++){
            curr+=a[i][1];
            if(curr > capacity)return 0;
        }
        return 1;
    }
};