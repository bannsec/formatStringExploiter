#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

#define BUFSIZE 128

bool cont = true;
long int myVar = 0xdeadbeefbaadf00d;

int main() {
    setbuf(stdin,0);
    setbuf(stdout,0);

    char buf[BUFSIZE];

    while (cont) {
        printf("Input: ");
        fgets(buf,BUFSIZE,stdin);
        printf(buf);
        printf("myVar value is: 0x%lx\n",myVar);
    }
}
