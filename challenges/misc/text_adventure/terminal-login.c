#include<stdio.h>
#include<string.h>

int main() {


	char password[] = "something";

	char buf[256];

	gets(buf);

	printf("pas: %s\n", password);
	printf("buf: %s\n", buf);
	int res;

	res = strcmp(password, buf);

	printf("%d", res);

	if (res == 0) {
		printf("welcome\n"); 
	}
	else {
		printf("wrong password\n");
	}

	return 1;


}
