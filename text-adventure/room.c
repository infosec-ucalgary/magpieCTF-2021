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
};

// initializes a room and returns a pointer to the room 
struct room * initializeRoom(char *roomName, char *description) {
    struct room *r = malloc(sizeof(struct room));
    r->name = roomName;
    r->description = description;

    return r;
}

// creates the rooms for the game map and links them together
// returns a pointer to an array of room pointers
struct room ** initializeMap() {
    // create all game rooms 
    struct room ** map = (struct room **) malloc(5 * sizeof(struct room *));

    map[0] = initializeRoom("entrance", "You're in a room, but you don't know how you got here");
    map[1] = initializeRoom("main", "You are in a large space with doors to the N, S, E, and W");
    map[2] = initializeRoom("lab", "Broken computer equipment is everywhere, but one terminal continues to blink...");
    map[3] = initializeRoom("locked", "A locked safe sits on the north side of the room, protected by a complex-looking pin pad.");
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
   else {
      printf("I don't understand what you want to see.");
   }
}