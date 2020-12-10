/* Binary tree search iterator */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */



typedef struct {
    struct TreeNode *current;

} BSTIterator;


void    iter(struct TreeNode *node, struct TreeNode **result)
{
    struct TreeNode *r;

    r = node->right;

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

BSTIterator* bSTIteratorCreate(struct TreeNode* root) {
    BSTIterator *it;
    struct TreeNode result;
    struct TreeNode *ptr = &result;

    iter(root, &ptr);
    it = (BSTIterator*)calloc(1, sizeof(BSTIterator));
    it->current = result.right;
    return it;
}
