//Swarnim Sinha - 1217390967
//Anusha Kolan - 1217179574


#include"msgs.h"
struct Queue_struct *port[100];

void first_client() {
	int mess[10] = {1,2,3,4,5,6,7,8,9,10};
	int i=1;
	while(1){
		send_message(port[0], &mess[0], port[i]);
		struct payload_type payload = receive_message(port[i]);
		int size=sizeof(payload.message)/sizeof(payload.message[0]);
		printf("\nfirst_client result returned from server :\n");
		for(int i=0;i<size;i++)
			printf("%d  ",payload.message[i]);
		sleep(1);
	}
}

void second_client() {
	int message[10] = {10,9,8,7,6,5,4,3,2,1};
	int i=2;
	while(1){
		send_message(port[0], &message[0], port[i]);
		struct payload_type payload = receive_message(port[i]);
		int size=sizeof(payload.message)/sizeof(payload.message[0]);
		printf("\nsecond_client result returned from server :\n");
		for(int i=0;i<size;i++)
			printf("%d  ",payload.message[i]);
		sleep(1);
	}
}

void third_client() {
	int message[10] = {7,14,21,28,35,42,49,56,63,70};
	int i=3;
	while(1){
		send_message(port[0], &message[0], port[i]);
		struct payload_type payload = receive_message(port[i]);
		int size=sizeof(payload.message)/sizeof(payload.message[0]);
		printf("\nthird_client result returned from server :\n");
		for(int i=0;i<size;i++)
			printf("%d  ",payload.message[i]);
		sleep(1);
	}
}

void server() {
	while(1){
		struct payload_type payload = receive_message(port[0]);
		int message[10];
		int size=sizeof(payload.message)/sizeof(payload.message[0]);
		printf("\nServer received data from client :\n");
		for(int i=0;i<size;i++)
			printf("%d  ",payload.message[i]);
		for(int i=0;i<size;i++)
        message[i]=payload.message[i]+1;
		send_message(payload.client_port, &message[0], port[0]);
		sleep(1);	
	}
}

void main()
{
	for(int i=0;i<100;i++)
		port[i]=NewPort();
	start_thread(server);
	start_thread(first_client);
	start_thread(second_client);
	start_thread(third_client);
	run();
}
