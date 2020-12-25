/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void    iter(struct TreeNode *node, struct TreeNode **result)
{
    // struct TreeNode *l;
    struct TreeNode *r;

    r = node->right;
    // l = node->left;

    if (node->left != NULL)
        iter(node->left, result);

    node->left = NULL;
    node->right = NULL;
    (*result)->right = node;
    (*result) = node;
    if (r != NULL)
        iter(r, result);

    return ;
}

struct TreeNode* increasingBST(struct TreeNode* root){
    struct TreeNode result;

    result.right = NULL;

    struct TreeNode *ptr = &result;
    iter(root, &ptr);
    return result.right;
}
