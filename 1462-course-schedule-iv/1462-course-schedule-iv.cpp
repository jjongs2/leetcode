class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses,
                                     vector<vector<int>>& prerequisites,
                                     vector<vector<int>>& queries) {
        int q = queries.size();
        vector<bool> answer(q);
        vector<vector<bool>> is_req(numCourses,
                                    vector<bool>(numCourses, false));
        int via, v1, v2;

        for (auto& edge : prerequisites)
            is_req[edge[0]][edge[1]] = true;
        for (via = 0; via < numCourses; ++via)
            for (v1 = 0; v1 < numCourses; ++v1)
                for (v2 = 0; v2 < numCourses; ++v2)
                    is_req[v1][v2] =
                        is_req[v1][v2] || (is_req[v1][via] && is_req[via][v2]);
        for (int i = 0; i < q; ++i) {
            v1 = queries[i][0];
            v2 = queries[i][1];
            answer[i] = is_req[v1][v2];
        }
        return answer;
    }
};
