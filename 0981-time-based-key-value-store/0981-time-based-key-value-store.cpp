class TimeMap {
public:
    TimeMap() {}

    void set(string key, string value, int timestamp) {
        outer_map[key][timestamp] = value;
    }

    string get(string key, int timestamp) {
        const auto& inner_map = outer_map[key];
        if (inner_map.empty())
            return "";
        auto it = inner_map.upper_bound(timestamp);
        if (it == inner_map.begin())
            return "";
        return (--it)->second;
    }

private:
    unordered_map<string, map<int, string>> outer_map;
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */