class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        vector<string> result;
        ranges::sort(folder);
        auto it = folder.begin();
        while (it != folder.end()) {
            const string& prefix = *it++;
            result.push_back(prefix);
            while (it != folder.end() && it->size() > prefix.size() &&
                   (*it)[prefix.size()] == '/' &&
                   it->compare(0, prefix.size(), prefix) == 0)
                ++it;
        }
        return result;
    }
};
