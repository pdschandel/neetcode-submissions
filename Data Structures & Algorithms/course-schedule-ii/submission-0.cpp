class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adjanceyList(numCourses);
        vector<int> indegree(numCourses, 0);
        
        for (auto const & course : prerequisites) {
            adjanceyList[course[1]].push_back(course[0]);
            indegree[course[0]]++;
        }      
        
        queue<int> q; 
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0)
                q.push(i);
        }
        
        vector<int> result;  
        while (!q.empty()) {
            int n = q.front();
            result.push_back(n);
            q.pop();
            for (auto const &al : adjanceyList[n]) {
                indegree[al]--;
                if (indegree[al] == 0) {
                    q.push(al);
                }
            }
        }
        
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] != 0)
                return {};
        }
        
        return result; 
    }
};