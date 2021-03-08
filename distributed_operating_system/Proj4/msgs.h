#include"sem.h"

struct Queue_struct {
 int counter;
 struct message_buffer *head;
 Semaphore_t *producer, *consumer, *mutex;
};

struct payload_type {
	int message[10];
	struct Queue_struct *client_port;
};

struct message_buffer {
 struct payload_type payload;
 struct message_buffer *next;
};

struct Queue_struct* NewPort()
{
  struct Queue_struct* queue = (struct Queue_struct *) malloc(sizeof(struct Queue_struct));
  queue->head = NULL;
  queue->counter = 0;
  queue-> producer=CreateSem(10);
  queue-> mutex = CreateSem(1);
  queue-> consumer = CreateSem(0);
  return queue;
} 

void addToPort(struct Queue_struct* port,struct message_buffer* item)
{
       if(port == NULL)
       {
       	printf("Port is null \n");
        return;
       }
       P(port->producer);
       P(port->mutex);
       struct message_buffer *message_node = port->head;
       if(message_node == NULL) {
       	port -> head = item;
       } 
       else
       {
       		while(message_node->next != NULL)
       			message_node = message_node->next;
       		message_node->next = item;
       }
       V(port->mutex);
       V(port->consumer);
}

struct payload_type deleteQueue(struct Queue_struct *port) {
	if(port == NULL)
    {
        printf("Port is null \n");
		return;
	}
	P(port->consumer);
    P(port->mutex);
	struct payload_type payload = port->head->payload;
	port->head = port->head->next;
	V(port->mutex);
    V(port->producer);
	return payload;

}

struct message_buffer * createItem(int *message, struct Queue_struct *client_port)
{
	struct message_buffer * item = (struct message_buffer *) malloc(sizeof(struct message_buffer));
	for(int i=0; i<10; i++)
		item->payload.message[i]=*(message+i);
	item->payload.client_port = client_port;
	item->next = NULL;
	return item;
}

void send_message(struct Queue_struct * port, int *message, struct Queue_struct *cport)
{
	struct message_buffer * node = createItem(message, cport);
	return addToPort(port, node);
}

struct payload_type receive_message(struct Queue_struct *port)
{
	return deleteQueue(port);
}
