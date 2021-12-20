#include "lists.h"

/**
 * check_cycle - function that detects a cycle list
 * @list: pointer to a list
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *non = list;
	listint_t *par = list;

	if (!list)
		return (0);
	while (par && par->next)
	{
		non = non->next;
		par = par->next->next;
		if (non == par)
			return (1);
	}
	return (0);
}
