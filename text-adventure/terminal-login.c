#include<stdio.h>
#include<stdlib.h>

void printflag(){
    printf("flag!\n");
}


int main(){
    printf("Give me a number\n");

    char buf[10];
    gets(buf, stdin);

    printf("Thanks!\n");
}