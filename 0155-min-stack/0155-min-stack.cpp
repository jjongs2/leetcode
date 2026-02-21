class MinStack {
public:
    MinStack() { stk.emplace(INT_MAX, INT_MAX); }

    void push(int val) {
        int top_min = stk.top().second;
        stk.emplace(val, min(val, top_min));
    }

    void pop() { stk.pop(); }

    int top() { return stk.top().first; }

    int getMin() { return stk.top().second; }

private:
    stack<pair<int, int>> stk;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
