#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<openssl/md5.h>

#ifndef FLAG_HASH
	#define FLAG_HASH "fake_flag"
#endif

void createHash(unsigned char *input, unsigned char *string_result) {
	unsigned char digest[MD5_DIGEST_LENGTH];
    MD5(input, (unsigned long) strlen(input), digest);
 
	for(int i = 0; i < 16; i++) {
        sprintf(&string_result[i*2], "%02x", (unsigned int)digest[i]);
	}
}

int main(){
	char string_result[33];
	char *flag = FLAG_HASH;
	
	printf("Give me a flag and I'll tell you if it's real.\n");

	char guess[100];
	fgets(guess, 100, stdin);

	createHash(guess, string_result);

	if (strncmp(flag, string_result, sizeof(FLAG_HASH)) == 0) {
		printf("That is just the flag I wanted!\n");
	} else {
		printf("I don't think that's a real flag...\n");
	}

	return 0;
}