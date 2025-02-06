class Solution {
public:
    int find(int v, vector<int>& parents) {
        int p;

        while ((p = parents[v]) != v) {
            parents[v] = parents[p];
            v = parents[p];
        }
        return v;
    }

    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int a, b, pa, pb;
        int n = edges.size();
        vector<int> parents(n + 1);

        for (int i = 1; i <= n; ++i)
            parents[i] = i;
        for (const auto& edge : edges) {
            a = edge[0];
            b = edge[1];
            pa = find(a, parents);
            pb = find(b, parents);
            if (pa == pb)
                return edge;
            parents[pa] = pb;
        }
        return {};
    }
};
