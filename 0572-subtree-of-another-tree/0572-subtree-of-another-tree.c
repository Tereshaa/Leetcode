/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool sametree(struct TreeNode* root, struct TreeNode* subRoot) {
    if (root == NULL || subRoot == NULL) {
        return root == subRoot;
    }
    return (root->val == subRoot->val) && sametree(root->left, subRoot->left) && sametree(root->right, subRoot->right);
}

bool isSubtree(struct TreeNode* root, struct TreeNode* subRoot) {
    if (!subRoot) {
        return true;
    }
    if (!root) {
        return false;
    }
    if (sametree(root, subRoot)) {
        return true;
    }
    return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
}

