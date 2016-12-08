#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>

bool cont = true;
int myVar = 0xdeadbeef;

int main() {
    setbuf(stdin,0);
    setbuf(stdout,0);

    char buf[64];

    while (cont) {
        strncpy(buf,"Hello, ",64);
        printf("Input: ");
        fgets(buf+7,64-7,stdin);
        printf(buf);
        printf("myVar value is: 0x%x\n",myVar);
    }
}
