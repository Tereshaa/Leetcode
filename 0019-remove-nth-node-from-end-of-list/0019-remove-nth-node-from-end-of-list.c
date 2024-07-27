/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    
    //basic approach
//     int count=0;
//     struct ListNode* temp =head;
//     while(temp!=NULL){
//         count=count+1;
//         temp=temp->next;  
//     }
//     int targetindex=count-n;
//     temp=head;
//     for(int i=1;i<targetindex;i++){
//         temp=temp->next;
//     }
//     struct ListNode* del = temp->next;
//     temp->next=del->next;
//     free(del);
    
//     if(targetindex==0){
//         struct ListNode* delhead=head->next;
//         head->next=delhead->next;
//         free(delhead);
//     }
//     return head;
    
    
    //optimal approach
    struct ListNode* dummy = malloc(sizeof(struct ListNode));
    dummy->next=head;
    struct ListNode* slow = dummy;
    struct ListNode* fast=dummy;
    for (int i=0;i<n;i++){
        fast=fast->next;
    }
    while(fast->next!=NULL){
        slow=slow->next;
        fast=fast->next;
    }
    
    struct ListNode* remove=slow->next;
    slow->next=remove->next;
    free(remove);
    return dummy->next;
    
}