/* Team Member 1 : Swarnim Sinha - 1217390967
   Team Member 2 : Anusha Kolan - 1217179574
*/

#include <stdio.h>
#include <unistd.h>
#include "threads.h"

int generic_variable = 0;

void function_1(){
    int func_specific = 0;
    printf("!!!!  function_1 STARTING !!!! \n");
    while(1){
        printf("Global variable value is : %d\n",generic_variable);
        printf("function_1 Local variable value is %d\n \n",func_specific);
        func_specific = func_specific + 1;
        generic_variable = generic_variable + 1;
        sleep(1);
        yield();
    }
}

void function_2(){
    int func_specific = 0;
    printf("!!!! function_2 STARTING !!! \n");
    while(1){
        printf("Global variable value is : %d\n",generic_variable);
        printf("function_2 Local variable value is %d\n \n",func_specific);
        func_specific = func_specific + 1;
        generic_variable = generic_variable + 1;
        sleep(1);
        yield();
    }
}

void function_3(){
    int func_specific = 0;
    printf("!!!! function_3 STARTING !!!! \n");
    while(1){
        printf("Global variable value is : %d\n",generic_variable);
        printf("function_3 Local varibale value is %d\n \n",func_specific);
        func_specific = func_specific + 1;
        generic_variable = generic_variable + 1;
        sleep(1);
        yield();
    }
}

int main(){

    ReadyQ = newQueue();
    start_thread(function_1);
    start_thread(function_2);
    start_thread(function_3);
    run();
    return 0;
}
