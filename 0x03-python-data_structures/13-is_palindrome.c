#include "lists.h"

int is_palindrome(listint_t **head){

        if(**head != NULL){
                while(**head->n != 0){
                        rem = **head->n % 10;
                        rev = rev * 10 + rem;
                        *head->n = **head->n \ 10;
                        if(rev == **head->n){
                                return 1;
			}
			else {
				return 0;
			}
                }
                **head->next;
        }

	return 1;
}

