#include "threads.h"

typedef struct Sem{
	int count;
	TCB_t * head;
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
		TCB_t * del = DelQueue(&ReadyQ);					// delete from the ReadyQ
		ReadyQ = queue1;
		AddQueue(&(sem->head),&del);						// add to SemQ
		if(sem->head == NULL){
			sem->head = queue1;
		}
		swapcontext(&(del->context),&(ReadyQ->context));	// swapcontext
	}
}

void V(Semaphore_t * sem){
	sem->count++;
	if(sem->count <= 0){
		//TCB_t * del = DelQueue(sem->head);				// delete from SemQ
		TCB_t * del = DelQueue(&(sem->head));				// delete from SemQ
		sem->head = queue1;
		AddQueue(&ReadyQ,&del);							// add to ReadyQ
		if(ReadyQ == NULL){
			ReadyQ = queue1;
		}
	}
	yield();
}
