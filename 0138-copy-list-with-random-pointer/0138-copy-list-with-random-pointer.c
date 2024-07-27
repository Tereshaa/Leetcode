/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     struct Node *next;
 *     struct Node *random;
 * };
 */

struct Node* copyRandomList(struct Node* head) {
    if (!head) return NULL;

    struct Node* temp = head;
    // copying list
    while (temp != NULL) {
        struct Node* copynode = (struct Node*)malloc(sizeof(struct Node));
        copynode->val = temp->val;
        copynode->next = temp->next;
        temp->next = copynode;
        temp = copynode->next;
    }
    
    // copying random pointers
    struct Node* current = head;
    while (current != NULL) {
        if (current->random != NULL) {
            current->next->random = current->random->next;
        } else {
            current->next->random = NULL;
        }
        current = current->next->next;
    }
    
    // seperating list
    struct Node* dummyNode = (struct Node*)malloc(sizeof(struct Node));
    struct Node* result = dummyNode;
    struct Node* temp1 = head;
    
    while (temp1 != NULL) {
        dummyNode->next = temp1->next;
        temp1->next = temp1->next->next;
        dummyNode = dummyNode->next;
        temp1 = temp1->next;
    }
    
    struct Node* copyHead = result->next;
    free(result); 
    return copyHead;
}


