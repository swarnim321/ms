#include "threads.h"
typedef struct Sem{
	int count;
	TCB_t * head;
}Semaphore_t;

void P(Semaphore_t * semaphore){
    TCB_t * deleted;
	semaphore->count--;
	if(semaphore->count < 0){
		deleted = DelQueue(&ReadyQ);
		ReadyQ = queue1;
		AddQueue(&(semaphore->head),&deleted);
		if(semaphore->head == NULL){
			semaphore->head = queue1;
		}
		swapcontext(&(deleted->context),&(ReadyQ->context));
	}
}

void V(Semaphore_t * semaphore){
    TCB_t * deleted;
	semaphore->count++;
	if(semaphore->count <= 0){
		deleted = DelQueue(&(semaphore->head));
		semaphore->head = queue1;
		AddQueue(&ReadyQ,&deleted);
		if(ReadyQ == NULL){
			ReadyQ = queue1;
		}
	}
	yield();
}

Semaphore_t * CreateSem(int initvalue){
	Semaphore_t * semaphore = (Semaphore_t *)malloc(sizeof(Semaphore_t));
	semaphore->count = initvalue;
	semaphore->head = NULL;
	return semaphore;
}
