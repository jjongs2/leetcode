class TimeMap {
public:
    TimeMap() {}

    void set(string key, string value, int timestamp) {
        store[key].emplace_back(timestamp, value);
    }

    string get(string key, int timestamp) {
        if (store.find(key) == store.end() || timestamp < store[key][0].first)
            return "";

        const auto& vec = store[key];
        int low = 0;
        int high = vec.size();

        while (high - low > 1) {
            int mid = (low + high) / 2;

            if (vec[mid].first <= timestamp) {
                low = mid;
            } else {
                high = mid;
            }
        }
        return vec[low].second;
    }

private:
    unordered_map<string, vector<pair<int, string>>> store;
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
