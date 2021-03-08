#include "q.h"
TCB_t * ReadyQ = NULL;
TCB_t * Curr_Thread = NULL;
int t_counter =1 ;
void start_thread(void (*function)(void))
{
     void *stackP = (void *)malloc(8192);
     TCB_t * tcb = (TCB_t *)malloc(sizeof(TCB_t));
     init_TCB(tcb, function, stackP, 8192);
     t_counter++;
     AddQueue(&ReadyQ,&tcb);
     ReadyQ=queue1;
}
void run()
{
	Curr_Thread=ReadyQ;
    ReadyQ=queue1;
    ucontext_t parent;                              // get a place to store the main context, for faking
    getcontext(&parent);                            // magic sauce
    swapcontext(&parent, &(Curr_Thread->context));  // start the first thread
}

void yield(){    
  TCB_t * Prev_Thread;
  Prev_Thread = ReadyQ;
  ReadyQ = rotateQueue(ReadyQ);
  Curr_Thread = ReadyQ;
  swapcontext(&(Prev_Thread->context), &(Curr_Thread->context));
}

