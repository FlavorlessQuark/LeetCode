/* Maximum Depth of Binary Tree */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int recurse(struct TreeNode *root, int depth)
{
    int left;
    int right;

    left = depth;
    right = depth;
    if (root->left != NULL)
        left = recurse(root->left, depth + 1);
    if (root->right != NULL)
        right = recurse(root->right, depth + 1);
     return (right > left) ? (right) : (left);
}

int maxDepth(struct TreeNode* root){
    if (root == NULL)
        return 0;
    return recurse(root, 1);
}
