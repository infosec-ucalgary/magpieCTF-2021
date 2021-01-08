#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void gen_enc_matrix(unsigned char matrix[][2]) {
	srand(time(0));

	while((matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]) % 2 == 0) {
		matrix[0][0] = rand() % 256;
		matrix[0][1] = rand() % 256;
		matrix[1][0] = rand() % 256;
		matrix[1][1] = rand() % 256;
	}

	return;
}

void encrypt_file(unsigned char matrix[][2], char * buffer, long flen) {
	char x, y;
	for(int i = 0;i < flen; i = i+2) {
		x = (matrix[0][0]*buffer[i]+matrix[0][1]*buffer[i+1]) % 256;
		y = (matrix[1][0]*buffer[i]+matrix[1][1]*buffer[i+1]) % 256;
		buffer[i]=x;
		buffer[i+1]=y;
	}
}

void write_file(char * filename, char * buffer, long flen) {
	FILE * f;
	
	f = fopen(filename, "wb");

	for(int i = 0;i < flen;i++) {
		fputc(buffer[i], f);
	}

	fclose(f);
}

int main(int argc, char * argv[]) {

	if(argc < 2) {
		printf("You have to specify a picture to print!");
		return 0;
	}

	unsigned char enc_matrix[2][2] = {{0,0},{0,0}};
	gen_enc_matrix(enc_matrix);

	FILE *f;
	long flen;
	f = fopen(argv[1], "rb");
	fseek(f, 0, SEEK_END);
	flen = ftell(f);
	rewind(f);

	char * buffer;
	buffer=(char *)malloc(flen * sizeof(char));
	fread(buffer, flen, 1, f);
	fclose(f);

	encrypt_file(enc_matrix, buffer, flen);

	write_file(argv[1], buffer, flen);

	return 0;
}
