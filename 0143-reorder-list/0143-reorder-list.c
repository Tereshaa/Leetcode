/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void reorderList(struct ListNode* head) {
     if (!head || !head->next){
         return;
     };
    struct ListNode* slow=head;
    struct ListNode* fast=head;

    while (fast!=NULL && fast->next!=NULL){
        slow=slow->next;
        fast=fast->next->next;
    }
    struct ListNode* second=slow->next;
    slow->next=NULL;
    struct ListNode* prev=NULL;
    
    while(second){
        struct ListNode* front=second->next;
        second->next=prev;
        prev=second;
        second=front;
    }
    struct ListNode* first=head;
    second=prev;
    while(second){
        struct ListNode* front1=first->next;
        struct ListNode*second1=second->next;
        first->next=second;
        second->next=front1;
        first=front1;
        second=second1;
    }  
}


