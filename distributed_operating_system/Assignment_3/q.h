#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "TCB.h"

Node * nq = NULL;

Node * newItem(Node * tcb){
	Node * newnode = (Node * )malloc(sizeof(Node));
	newnode->next = newnode;
	newnode->prev = newnode;
	newnode->context = tcb->context;
	newnode->thread_id = tcb->thread_id;
	return newnode;
}

Node * newQueue(){
  Node * head = NULL;
  return head;
}

void AddQueue(Node * head, Node * tcb){
   if(head == NULL){
    nq = newItem(tcb);
    return;
  }
  Node * newnode = newItem(tcb);
  Node * t = head->prev;  
  newnode->next = head;
  head->prev = newnode;
  newnode->prev = t;
  t->next = newnode;
}

Node * rotateQueue(Node * head){
	if(head == NULL){
    exit(0);
    return NULL;
  	}
	head = head->next;
	return head;
}

Node * DelQueue(Node * head){ 
  if(head == NULL){
    printf("Can't delete as head is NULL. Exiting\n");
    exit(0);
    return NULL;
  }
  if(head == head->next){                 
    nq = NULL;
    return head;
  }
  Node * del = head;
  Node * t = head->prev;    
  head = head->next;    
  head->prev = t;
  t->next = head;

  del->next = del;
  del->prev = del;
  nq = head;
  return del;    
}
