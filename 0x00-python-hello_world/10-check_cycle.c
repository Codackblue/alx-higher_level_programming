#include "lists.h"

/**
 * check_cycle - check for loop in LL
 * @l: head of linked list
 *
 * Description - check for loops in LL
 * Return: 1 if cycled, 0 if not
 */

int check_cycle(listint_t *l)
{
	listint_t *slow, *fast;

	if (!l)
	{
		return (0);
	}
	slow = l;
	fast = l->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
