/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isBalanced(struct TreeNode* root) {
    return height(root)!=-1;

}

 int height(struct TreeNode* root){
        if (root==NULL){
            return 0;
        }
        int lh= height(root->left);
        if(lh==-1) return -1;
        int rh=height(root->right);
        if(rh==-1) return -1;
        
        if (abs(lh-rh)>1) return -1;
        return 1+(lh>rh?lh:rh);
    }