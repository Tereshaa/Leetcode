/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int diameterOfBinaryTree(struct TreeNode* root) {
    int diameter=0;
    height(root,&diameter);
    return diameter;
}

int height(struct TreeNode* root,int *diameter){
    if(root==NULL) return 0;
    int lh=height(root->left,diameter);
    int rh=height(root->right,diameter);
    *diameter=(*diameter>(lh+rh)? *diameter:(lh+rh));
    return 1+ (lh>rh?lh:rh);
    
}