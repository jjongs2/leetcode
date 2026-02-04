class Solution {
public:
    long long maxSumTrionic(vector<int>& nums) {
        long long result = numeric_limits<long long>::min();
        long long sum, max_sum, trionic_sum;
        int n = nums.size();
        int i = 0;
        int l, p, q, r;

        l = p = q = r = 0;
        while (i < n) {
            if (l < p && p < q && q < r) {
                l = q;
                p = r;
            } else {
                l = i++;

                while (i < n && nums[i - 1] < nums[i])
                    ++i;
                p = i - 1;
                if (p == l)
                    continue;
            }

            while (i < n && nums[i - 1] > nums[i])
                ++i;
            q = i - 1;
            if (q == p)
                continue;

            while (i < n && nums[i - 1] < nums[i])
                ++i;
            r = i - 1;
            if (r == q)
                continue;

            max_sum = sum = 0;
            for (int j = p - 2; j >= l; --j) {
                sum += nums[j];
                max_sum = max(max_sum, sum);
            }
            trionic_sum = max_sum;

            for (int j = p - 1; j <= q + 1; ++j) {
                trionic_sum += nums[j];
            }

            max_sum = sum = 0;
            for (int j = q + 2; j <= r; ++j) {
                sum += nums[j];
                max_sum = max(max_sum, sum);
            }
            trionic_sum += max_sum;

            result = max(result, trionic_sum);
        }
        return result;
    }
};
