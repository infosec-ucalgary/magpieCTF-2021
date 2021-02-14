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
            executeLook("around", currRoom);
            system("clear");
        }
        else if (strcmp(verb, "help") == 0) {
            printf("Usage: [verb] [noun]\n"
                "Some helpful commands (there may be more!)\n"
                "\thelp: print this help dialogue\n"
                "\tlook: inspect a room or an item\n"
                "\tgo: move in a given direction\n"
                "\tuse: use an object\n"
                "\tclear: clear the screen\n"
                "\tquit: leave the game\n"
                "Some examples:\n"
                "\t-->look around: provide a description of your current room\n"
                "\t-->go north: move to the room north of your current room\n");
        }
        else if (strcmp(verb, "look") == 0) {
            executeLook(noun, currRoom);
        }
        else if (strcmp(verb, "go") == 0) {
            executeGo(noun, currRoom);
        }
		else if (strcmp(verb, "use") == 0) {
			executeUse(noun, currRoom);
		}
        else {
            printf("I don't know how to '%s'.\n", verb);
        }
    }
    return true;
}
