#include <stdio.h>
#include <string.h> 
#include <stdlib.h>
#include "room.h" 

struct room {
    char *name;
    char *description;
    struct room *northLink;
    struct room *southLink;
    struct room *westLink;
    struct room *eastLink;

    struct item *items[5];
};

struct item {
    char *name;
    char *description;
    char *effect;
    int executable;
};

// Function header
int roomHasItem(const char *, struct room *);

// initializes an item and returns a pointer to the item 
struct item *initializeItem(char *itemName, char *description, char *effect, int executable) {
    struct item *it = malloc(sizeof(struct item));
    it->name = itemName;
    it->description = description;
    it->effect = effect;
    it->executable = executable;

    return it;
}

// initializes a room and returns a pointer to the room 
struct room * initializeRoom(char *roomName, char *description) {
    struct room *r = malloc(sizeof(struct room));
    r->name = roomName;
    r->description = description;

    for (int i=0; i<5; i++) {
        r->items[i] = initializeItem("", "There doesn't seem to be anything here", "Nothing happens", 0);
    }

    return r;
}

// creates the rooms for the game map and links them together
// returns a pointer to an array of room pointers
struct room ** initializeMap() {
    // create all game rooms 
    struct room ** map = (struct room **) malloc(5 * sizeof(struct room *));

    map[0] = initializeRoom("entrance", "You're in a room, but you don't know how you got here. To the north is a heavy metal door.");
    map[1] = initializeRoom("main", "You are in a large space with metal doors to the North, South, and West");
    map[2] = initializeRoom("lab", "To the east is a heavy metal door. Broken computer equipment is everywhere, but one terminal continues to blink...");
    map[3] = initializeRoom("locked", "A locked safe sits on the north side of the room. To the south is a heavy metal door.");
    map[4] = initializeRoom("secret", "You're not sure you're supposed to be here...");

    // create links between rooms
    map[0]->northLink = map[1];

    map[1]->northLink = map[3];
    map[1]->southLink = map[0];
    map[1]->westLink = map[2];
    map[1]->eastLink = map[4];

    map[2]->eastLink = map[1];

    map[3]->southLink = map[1];

    map[4]->westLink = map[1];

    // add items to rooms 
    map[2]->items[0] = initializeItem("terminal", "One computer in the back corner appears to still be functioning. It glows green and a single cursor blinks.", "./terminal-login", 1);
    map[2]->items[1] = initializeItem("junk", "Heaped around the room are piles of broken circuitry and smashed hardware. None of it seems useable.", "Nothing happens", 0);

    map[3]->items[0] = initializeItem("safe", "The grey metal safe takes up the whole wall. On the front is a large black wheel and a complicated pinpad.", "Nothing happens", 0);
    map[3]->items[1] = initializeItem("pinpad", "The pinpad consists of nine worn buttons and a faded day-glo screen.", "Nothing happens", 0);

    // return array of rooms 
    return map;
}

void executeGo(const char *noun, struct room *currRoom) {
    if (noun != NULL && strcmp(noun, "north") == 0) {
        if (currRoom->northLink == NULL){
            printf("You can't go that way in here.");
        } 
        else {
            *currRoom = *currRoom->northLink;
            printf("%s", currRoom->description);
        }
    }
    else if (noun != NULL && strcmp(noun, "south") == 0) {
        if (currRoom->southLink == NULL){
            printf("You can't go that way in here.");
        }
        else {
            *currRoom = *currRoom->southLink;
            printf("%s", currRoom->description);
        }
    }
    else if (noun != NULL && strcmp(noun, "east") == 0) {
        if (currRoom->eastLink == NULL){
            printf("You can't go that way in here.");
        }
        else {
            *currRoom = *currRoom->eastLink;
            printf("%s", currRoom->description);
        }
    }
    else if (noun != NULL && strcmp(noun, "west") == 0) {
        if (currRoom->westLink == NULL){
            printf("You can't go that way in here.");
        }
        else {
            *currRoom = *currRoom->westLink;
            printf("%s", currRoom->description);
        }
    }
    else {
      printf("I don't understand where you want to go.");
   }
}

void executeLook(const char *noun, struct room *currRoom) {
    if (noun != NULL && strcmp(noun, "around") == 0) {
      printf("%s", currRoom->description);
    }
    else if (noun != NULL) {
        for (int i=0; i<5; i++) {
            if (noun != "" && strcmp(noun, currRoom->items[i]->name) == 0) {
               printf("%s", currRoom->items[i]->description);
               return;
            }
        }
        printf("There doesn't seem to be a(n) %s in here.", noun);
   }
   else {
      printf("I don't understand what you want to see.");
   }
}

void executeUse(const char * noun, struct room * currRoom) {
    int position = roomHasItem(noun, currRoom);
	if (position != -1) {
        if (currRoom->items[position]->executable == 1){
            // This means the item represents an external child process that
            // we should spin off the main program
            system(currRoom->items[position]->effect);
        }
        else {
            // This means the item does not need to spin off a child process
            printf("%s", currRoom->items[position]->effect);
        }
	} 
    else {
		printf("There is no %s in this room.", noun);
	}
}

/*
 * Item helper functions
 */

// Loop through non-null indices of the items and return
// if the item name matches the given noun
int roomHasItem(const char * name, struct room * rm) {
	for (int i = 0; i < 5; i++) {
		if (!rm->items[i]) 
            return -1;
		else {
			if (strcmp(rm->items[i]->name, name) == 0) {
				return i;
			}
		}
	}
	return -1;
}
