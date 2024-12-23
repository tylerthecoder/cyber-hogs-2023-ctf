#include <time.h>
#include <stdio.h>
#include <stdlib.h>

char cmd[13] = { 0 };
int cmdPtr = 0;

void pwn() {
    printf("What's your name: ");

    char s[20];
    fgets(s, 100, stdin);
    printf("Hello %s!\n", s);
}

void p1() {
    cmd[cmdPtr+0] = 'f';
    cmd[cmdPtr+1] = 'l';
    cmd[cmdPtr+2] = 'a';
    cmd[cmdPtr+3] = 'g';
    cmdPtr += 4;
}

void p2() {
    cmd[cmdPtr+0] = '.';
    cmd[cmdPtr+1] = 't';
    cmd[cmdPtr+2] = 'x';
    cmd[cmdPtr+3] = 't';
    cmdPtr += 4;
}

void p3() {
    cmd[cmdPtr+0] = 'c';
    cmd[cmdPtr+1] = 'a';
    cmd[cmdPtr+2] = 't';
    cmd[cmdPtr+3] = ' ';
    cmdPtr += 4;
}

void p4() {
    system(cmd);
}

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    pwn();

    return 0;
}