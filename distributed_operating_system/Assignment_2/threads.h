#include "q.h"
TCB_t * ReadyQ = NULL;
TCB_t * Curr_Thread = NULL;
int t_counter = 1;
void start_thread(void (*function)(void))
{
     void *stackP = (void *)malloc(8192);
     TCB_t * tcb = (TCB_t *)malloc(sizeof(TCB_t));
     init_TCB(tcb, function, stackP, 8192);
     tcb->thread_id = t_counter;
     t_counter++;
     ReadyQ = queue1;
     AddQueue(&ReadyQ,&tcb);
}
void run()
{
    Curr_Thread = DelQueue(&ReadyQ);
    ReadyQ=queue1;
    ucontext_t parent;                              // get a place to store the main context, for faking
    getcontext(&parent);                            // magic sauce
    swapcontext(&parent, &(Curr_Thread->context));  // start the first thread
}
void yield(){
  TCB_t * Prev_Thread;
  AddQueue(&ReadyQ, &Curr_Thread);
  Prev_Thread = Curr_Thread;
  Curr_Thread = DelQueue(&ReadyQ);
  ReadyQ=queue1;
  swapcontext(&(Prev_Thread->context), &(Curr_Thread->context));
}
