#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

#define BUFSIZE 1024

bool cont = true;
char myVar[128] = "Hello";

int main() {
    setbuf(stdin,0);
    setbuf(stdout,0);

    char buf[BUFSIZE];

    while (cont) {
        printf("Input: ");
        fgets(buf,BUFSIZE,stdin);
        printf(buf);
        printf("myVar value is: %s\n",myVar);
    }
}
