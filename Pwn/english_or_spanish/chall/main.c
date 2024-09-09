// gcc -no-pie -fno-stack-protector -o main main.c 
#include <stdio.h>
#include <stdlib.h>

void input(const char *msg, char *ptr, int len){
	printf("%s", msg);
	ssize_t recv = 0;
	while (recv < len){
		if (read(0, &ptr[recv], 1) < 0) exit(1);
		if (ptr[recv] == '\n'){
			ptr[recv] = '\0';
			break;
		} recv++;
	}
}

int main(){
	char buf[0x50];
	input("English or Spanish?\nWhoever pwning first is gay\nQuien juegue primero es gay\n> ", buf, sizeof(buf)*2);
	return 0;
}

__attribute__((constructor))
void setup(void){
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
}
