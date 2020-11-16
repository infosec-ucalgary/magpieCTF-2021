#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include "room.h"

bool parseAndExecute(char *input, struct room *currRoom) {
    char *verb = strtok(input, " \n");
    char *noun = strtok(NULL, " \n");

    if (verb != NULL) {
        if (strcmp(verb, "quit") == 0) {
            return false;
        }
        else if (strcmp(verb, "clear") == 0) {
            system("clear");
        }
        else if (strcmp(verb, "look") == 0) {
            executeLook(noun, currRoom);
        }
        else if (strcmp(verb, "go") == 0) {
            executeGo(noun, currRoom);
        }
        else {
            printf("I don't know how to '%s'.\n", verb);
        }
    }
    return true;
}
