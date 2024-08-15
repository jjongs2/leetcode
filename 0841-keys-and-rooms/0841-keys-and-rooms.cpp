#include <algorithm>
#include <stack>
#include <vector>

class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool> visited(n);
        stack<int> s{{0}};

        visited[0] = true;
        while (!s.empty()) {
            int v0 = s.top();
            s.pop();
            for (int v : rooms[v0]) {
                if (visited[v])
                    continue;
                visited[v] = true;
                s.push(v);
                n -= 1;
            }
        }
        return n == 1;
    }
};
