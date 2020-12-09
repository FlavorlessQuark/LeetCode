/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2)
{
    if (l1 == NULL)
        return l2;
    if (l2 == NULL)
        return l1;
    if (!l1 && !l2 )
        return NULL;
    struct ListNode *ret = NULL, *tmp = NULL;

    tmp = calloc(1,sizeof(struct ListNode));
    ret = tmp;

    while (1)
    {
        if (l1)
        {
            tmp->val += l1->val;
            l1 = l1->next;
        }
        if (l2)
        {
            tmp->val += l2->val;
            l2 = l2->next;
        }
        if (l1 || l2 || (tmp->val >= 10))
        {
            tmp->next = calloc(1, sizeof(struct ListNode));
            if (tmp->val >= 10)
            {
                tmp->next->val = 1;
                tmp->val -= 10;
            }
        }
         else break ;
        tmp = tmp->next;
    }
    return ret;
}
