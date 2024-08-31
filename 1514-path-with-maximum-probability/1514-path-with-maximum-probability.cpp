#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges,
                          vector<double>& succProb, int start_node,
                          int end_node) {
        vector<vector<pair<int, double>>> adj(n);
        for (int i = edges.size() - 1; i >= 0; --i) {
            const auto& edge = edges[i];
            adj[edge[0]].emplace_back(edge[1], succProb[i]);
            adj[edge[1]].emplace_back(edge[0], succProb[i]);
        }
        vector<double> probs(n, 0.0);
        probs[start_node] = 1.0;
        priority_queue<pair<double, int>> pq;
        pq.emplace(1.0, start_node);
        while (!pq.empty()) {
            auto [prob1, v1] = pq.top();
            if (v1 == end_node)
                return prob1;
            pq.pop();
            if (prob1 < probs[v1])
                continue;
            for (auto [v2, prob2] : adj[v1]) {
                prob2 *= prob1;
                if (prob2 > probs[v2]) {
                    probs[v2] = prob2;
                    pq.emplace(prob2, v2);
                }
            }
        }
        return 0.0;
    }
};
