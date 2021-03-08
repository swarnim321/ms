#include "threads.h"

typedef struct Sem{
	int count;
	Node * head;
}Semaphore_t;

Semaphore_t * CreateSem(int initvalue){
	Semaphore_t * sem = (Semaphore_t *)malloc(sizeof(Semaphore_t));
	sem->count = initvalue;
	sem->head = NULL;
	printf("Created semaphore initialised to %d\n",initvalue);
	return sem;
}

void P(Semaphore_t * sem){
	sem->count--;
	if(sem->count < 0){
		Node * del = DelQueue(ReadyQ);					// delete from the ReadyQ
		ReadyQ = nq;
		AddQueue(sem->head,del);						// add to SemQ
		if(sem->head == NULL){
			sem->head = nq;
		}
		swapcontext(&(del->context),&(ReadyQ->context));	// swapcontext
	}
}

void V(Semaphore_t * sem){
	sem->count++;
	if(sem->count <= 0){
		Node * del = DelQueue(sem->head);				// delete from SemQ
		sem->head = nq;
		AddQueue(ReadyQ,del);							// add to ReadyQ
		if(ReadyQ == NULL){
			ReadyQ = nq;
		}
	}
	yield();
}
