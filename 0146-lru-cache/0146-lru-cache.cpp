class LRUCache {
public:
    LRUCache(int capacity) { cap_ = capacity; }

    int get(int key) {
        if (iters_.find(key) == iters_.end()) {
            return -1;
        }
        lst_.splice(lst_.begin(), lst_, iters_[key]);
        return iters_[key]->second;
    }

    void put(int key, int value) {
        if (iters_.find(key) != iters_.end()) {
            iters_[key]->second = value;
            lst_.splice(lst_.begin(), lst_, iters_[key]);
            return;
        }
        if (lst_.size() == cap_) {
            iters_.erase(lst_.back().first);
            lst_.pop_back();
        }
        lst_.emplace_front(key, value);
        iters_[key] = lst_.begin();
    }

private:
    int cap_;
    list<pair<int, int>> lst_;
    unordered_map<int, list<pair<int, int>>::iterator> iters_;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
