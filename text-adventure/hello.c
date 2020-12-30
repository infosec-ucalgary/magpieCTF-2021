#include<stdio.h>
#include<stdlib.h>

int main(){
    printf("give me a number\n");

    char buff[5];
    fgets(buff, sizeof(buff), stdin);

    printf("thanks for the number! returning to parent process (i hope)\n");

    return 0;
}