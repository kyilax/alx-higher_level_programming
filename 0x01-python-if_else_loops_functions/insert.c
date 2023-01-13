#include "lists.h"
listint_t *insert_node(listint_t **head, int number){
	listint_t *new;
	char *temp;

	new = malloc(sizeof(listint_t));
	if(new == NULL){
		return NULL;
	}

	new->n = n;

	while(*head != NULL){
		if(*head->n < new->n){
			*head->next;
		} 
		else {
			temp = *head->next;
			*head->next = new;
			new->next = temp;	
		}
	}
}
