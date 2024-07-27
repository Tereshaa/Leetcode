/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* t1=l1;
    struct ListNode* t2=l2;
    struct ListNode* dummy = malloc(sizeof(struct ListNode));
    struct ListNode* current = dummy;
    int carry =0;
    while(t1!=NULL ||t2!=NULL){
        int sum = carry;
        if(t1){
            sum+=t1->val;
            t1=t1->next;
        }
        if(t2){
            sum+=t2->val;
            t2=t2->next;
        }
        struct ListNode* newnode=malloc(sizeof(struct ListNode));
        newnode->val=sum%10;
        carry=sum/10;
        current->next=newnode;
        current=current->next;
    }
    if(carry){
        struct ListNode* carry1=malloc(sizeof(struct ListNode));
        carry1->val=carry;
        carry1->next=NULL;
        current->next=carry1;
    }
    else{
        current->next=NULL;
    }
    struct ListNode* res=dummy->next;
    free(dummy);
    return res;
}
