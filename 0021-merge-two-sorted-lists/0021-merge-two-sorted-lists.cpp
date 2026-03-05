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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy;
        ListNode* node = &dummy;

        while (list1 && list2) {
            if (list2->val < list1->val) {
                node->next = list2;
                list2 = list2->next;
            } else {
                node->next = list1;
                list1 = list1->next;
            }
            node = node->next;
        }
        node->next = list1 ? list1 : list2;
        return dummy.next;
    }
};
