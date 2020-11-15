#include <stdio.h>
#include <stdbool.h>
#include "parsexec.h"
#include "room.h"

static char input[100] = "look around";

static bool getInput(void) {
    printf("\n--> ");
    return fgets(input, sizeof input, stdin) != NULL;
}

int main(){
    printf("Welcome to Magpie Adventure.\n");
    struct room **map = initializeMap();
    struct room *currRoom = map[0];         // player always starts at map position 0

    while (parseAndExecute(input, currRoom) && getInput());
    printf("\nBye!\n");

    return 0;
}