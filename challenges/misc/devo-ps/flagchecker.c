#include<stdio.h>
#include<string.h>

#define FLAG_HASH "flag\n"

char * createHash(char *input) {
	return input;
}

int main(){
	printf("Give me a flag and I'll tell you if it's real.\n");
	char * flag = FLAG_HASH;

	char guess[100];
	fgets(guess, 100, stdin);

	if (strncmp(createHash(guess), flag, sizeof(flag)) == 0) {
		printf("That is just the flag I wanted!\n");
	} else {
		printf("I don't think that's a real flag...\n");
	}

	return 0;
}