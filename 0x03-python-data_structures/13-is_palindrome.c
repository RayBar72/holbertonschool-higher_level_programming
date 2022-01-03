#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: double pointer of the list
 * Return: pointer to the first node of the reversed list
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *forward = NULL, *prev = NULL;

	while (*head)
	{
		forward = (*head)->next;
		(*head)->next = prev;
		prev = (*head);
		(*head) = forward;

	}
	(*head) = prev;
	return (*head);
}

/**
 * is_palindrome - funtion that check if a singly list is a palindrome
 * @head: pointer to pointer
 * Return - 1 if palindrome else 0
 */

int is_palindrome(listint_t **head)
{

	listint_t *orig = *head, *rev = NULL;

	if (!*head)
		return (1);
	rev = reverse_list(&orig);
	while (orig && rev)
	{
		if (orig->n != rev->n)
			return (0);
		orig = orig->next;
		rev = rev->next;
	}
	return (1);
}
