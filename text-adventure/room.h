extern struct room * initializeRoom(char *name, char *description);
extern struct room ** initializeMap();

extern void executeLook(const char *noun, struct room *currRoom);
extern void executeGo(const char *noun, struct room *currRoom);
extern void executeUse(const char *noun, struct room *currRoom);

