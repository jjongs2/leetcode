class DetectSquares {
public:
    void add(vector<int> point) {
        int x = point[0];
        int y = point[1];
        x_to_ys[x].insert(y);
        freq[encode(x, y)] += 1;
    }

    int count(vector<int> point) {
        int result = 0;
        int x0 = point[0];
        int y0 = point[1];

        for (int y : x_to_ys[x0]) {
            if (y == y0)
                continue;
            int d = abs(y - y0);
            for (int x : {x0 + d, x0 - d}) {
                result += freq[encode(x, y)] * freq[encode(x, y0)] *
                          freq[encode(x0, y)];
            }
        }
        return result;
    }

private:
    unordered_map<int, unordered_set<int>> x_to_ys;
    unordered_map<int, int> freq;

    int encode(int x, int y) { return 1001 * x + y; }
};

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares* obj = new DetectSquares();
 * obj->add(point);
 * int param_2 = obj->count(point);
 */
