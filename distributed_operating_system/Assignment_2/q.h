#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "TCB.h"

TCB_t * queue1 = NULL;
TCB_t * newItem()
{
    TCB_t *new = (TCB_t*)malloc(sizeof(TCB_t));
    return new;
}
TCB_t * newQueue()
{
    TCB_t * head = NULL;
    return head;
}
void AddQueue(TCB_t **head, TCB_t **item)
{
    if((*head) == NULL)
    {
       (*head) = (*item);
       (*head)->next = (*head)->prev;
       (*head)->prev = (*head)->next;
       queue1 = (*head);
       return;
    }
    if((*head)->next == NULL){
        (*head)->next = (*item);
        (*head)->prev = (*item);
        (*item)->next = (*head);
        (*item)->prev = (*head);
        queue1 = (*head);
        return;
    }
    TCB_t *holder;
    holder = (*head)->prev;
    (*item)->prev = holder;
    (*item)->next = (*head);
    holder->next = (*item);
    (*head)->prev = (*item);
    queue1 = (*head);
}
TCB_t * rotateQueue(TCB_t * head)
{
    if(head == NULL)
    {
        exit(0);
        return NULL;
    }
    head = head->next;
    return head;
}
TCB_t * DelQueue(TCB_t** head)
{
    if((*head) == NULL)
    {
        return NULL;
    }
    TCB_t *holder = (*head);
    if((*head)->next == NULL)
    {
        (*head)->next = NULL;
        (*head)->prev = NULL;
        queue1= (*head);
        return holder;
    }
    TCB_t *last = (*head);
    while((*head) != last->next)
    {
        last =last->next;
    }
    (*head) = holder->next;
    last->next = (*head);
    (*head)->prev = last;
    holder->next = NULL;
    holder->prev = NULL;
    queue1 = (*head);
    return holder;
}
