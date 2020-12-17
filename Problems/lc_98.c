#include <limits.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool validate(struct TreeNode *node, long min, long max)
{
    bool l;
    bool r;

    l = true;
    r = true;

    if (node == NULL)
        return true;
    // printf("Val, %d min %d max %d\n", node->val, min, max);
    if (node->val <= min || node->val >= max)
        return false;
    if (node->left)
        l = validate(node->left, min, node->val);
    if (l == false)
        return false;
    if (node->right)
       r = validate(node->right, node->val, max);
    return r;
}


bool isValidBST(struct TreeNode* root)
{
    if (root == NULL)
        return true;
    return validate(root->left, LONG_MIN, root->val) && validate(root->right, root->val, LONG_MAX);
}
