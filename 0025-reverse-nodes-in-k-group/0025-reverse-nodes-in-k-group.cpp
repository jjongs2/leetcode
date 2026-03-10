/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (k == 1)
            return head;

        ListNode dummy(0, head);
        ListNode* prev_tail = &dummy;

        auto find_curr_tail = [k](ListNode* node) -> ListNode* {
            for (int i = 0; (i < k) && (node != nullptr); ++i) {
                node = node->next;
            }
            return node;
        };

        while (true) {
            ListNode* curr_tail = find_curr_tail(prev_tail);
            if (curr_tail == nullptr)
                break;

            ListNode* curr_head = prev_tail->next;
            ListNode* next_head = curr_tail->next;
            ListNode* n1 = next_head;
            ListNode* n2 = curr_head;
            while (n2 != next_head) {
                ListNode* n3 = n2->next;
                n2->next = n1;
                n1 = n2;
                n2 = n3;
            }
            prev_tail->next = curr_tail;
            prev_tail = curr_head;
        }
        return dummy.next;
    }
};
