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

int bSTIteratorNext(BSTIterator* obj) {
    int val;
    val = obj->current->val;
    obj->current = obj->current->right;

    return val;
}

bool bSTIteratorHasNext(BSTIterator* obj) {
    return (obj->current == NULL) ? (false) :(true);
}

void bSTIteratorFree(BSTIterator* obj) {
    free(obj);
}

/**
 * Your BSTIterator struct will be instantiated and called as such:
 * BSTIterator* obj = bSTIteratorCreate(root);
 * int param_1 = bSTIteratorNext(obj);

 * bool param_2 = bSTIteratorHasNext(obj);

 * bSTIteratorFree(obj);
*/
