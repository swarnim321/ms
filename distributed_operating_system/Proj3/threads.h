#include "q.h"

Node * ReadyQ = NULL;
Node * Curr_Thread = NULL;

int thread_Count = 1;

/*void print_Tid(Node * tcb){
  printf("Thread_id is : %d\n\n",tcb->thread_id);
  return;
}*/

void start_thread(void (*function)(void))
{ 	 
     //printf("Inside start_thread : \n");
     void *stackP = (void *)malloc(8192);
     Node * tcb = (Node *)malloc(sizeof(Node));
     init_TCB(tcb, function, stackP, 8192);
     //tcb->thread_id = thread_Count;
     //thread_Count++;
     AddQueue(ReadyQ,tcb);
     ReadyQ = nq;               
}

void run()
{
    //printf("Inside run()\n");
    Curr_Thread = ReadyQ;
    ucontext_t parent;                              // get a place to store the main context, for faking
    getcontext(&parent);                            // magic sauce
    swapcontext(&parent, &(Curr_Thread->context));  // start the first thread
}

void yield(){   
  //printf("Inside yield()\n");  
  Node * Prev_Thread;
  Prev_Thread = ReadyQ;
  //print_Tid(Prev_Thread);
  ReadyQ = rotateQueue(ReadyQ);
  Curr_Thread = ReadyQ;
  swapcontext(&(Prev_Thread->context), &(Curr_Thread->context));
}
