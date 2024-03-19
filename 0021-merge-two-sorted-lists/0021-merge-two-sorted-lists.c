/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* first=list1;
    struct ListNode* second=list2;
    struct ListNode* result=malloc(sizeof(struct ListNode));
    struct ListNode* current=result;
    
    while(first!=NULL && second!=NULL){
        if(first->val <= second->val){
            current->next=first;
            first=first->next;
        }
        else{
            current->next=second;
            second=second->next;
        }
        current=current->next;
    }
     if (first != NULL) {
        current->next = first;
    } 
    else {
        current->next = second;
    }
    struct ListNode* ans=result->next;
    free(result);
    
    return ans;
  
}