// https://leetcode.com/problems/merge-two-sorted-lists/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
  ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
      
    // Empty list check 
    if (l1 == nullptr) return l2;
    if (l2 == nullptr) return l1;
    
    ListNode* dummy = new ListNode(-1);
    ListNode* l3 = dummy;
    
    while(l1 != nullptr && l2 != nullptr) {
      if(l1->val <= l2->val) {
        l3->next = l1;
        l1 = l1->next;
      } else {
        l3->next = l2;
        l2 = l2->next;
      }
      l3 = l3->next;
    }
    
    if(l1 == nullptr) {
      l3->next = l2;
    } else {
      l3->next = l1;
    }
    
    return dummy->next;
  }
};