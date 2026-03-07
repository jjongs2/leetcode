/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> to_copy;
        Node* curr = head;

        while (curr) {
            to_copy[curr] = new Node(curr->val);
            curr = curr->next;
        }

        curr = head;
        while (curr) {
            to_copy[curr]->next = to_copy[curr->next];
            to_copy[curr]->random = to_copy[curr->random];
            curr = curr->next;
        }
        return to_copy[head];
    }
};
