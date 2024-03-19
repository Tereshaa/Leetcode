/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    int count=0;
    struct ListNode* temp= head;
    while(temp!=NULL){
        count=count+1;
        temp=temp->next;
    }
    count=count/2;
    temp=head;
    for (int i=0;i<count;i++){
        temp=temp->next;
    }
    return temp;
    
}