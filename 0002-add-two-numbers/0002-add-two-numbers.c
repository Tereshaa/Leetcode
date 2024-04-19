/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* dummy =malloc(sizeof(struct ListNode));
    struct ListNode* temp = dummy;
    int carry =0;
    while( (l1!=NULL || l2!= NULL) || carry){
        int sum=0;
        if(l1!=NULL){
            sum=sum+l1->val;
            l1=l1->next;
        }
        if(l2!=NULL){
            sum=sum+l2->val;
            l2=l2->next;
        }
        sum=sum+carry;
        carry=sum/10;
        struct ListNode* number= malloc(sizeof(struct ListNode));
        number->val=sum%10;
        number->next=NULL;
        temp->next=number;
        temp=temp->next;
    }
    return dummy->next;
    
}