#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>

void addPrompt() {
    int a, b;
    printf("First number? ");
    scanf("%d", &a);
    printf("Second number? ");
    scanf("%d", &b);
    int result = a + b;
    printf("%d\n", result);
}

void subPrompt() {
    int a, b;
    printf("First number? ");
    scanf("%d", &a);
    printf("Second number? ");
    scanf("%d", &b);
    int result = a - b;
    printf("%d\n", result);
}

void mulPrompt() {
    int a, b;
    printf("First number? ");
    scanf("%d", &a);
    printf("Second number? ");
    scanf("%d", &b);
    int result = a * b;
    printf("%d\n", result);
}

void pwn() {
    char s[20];
    bool ignoreHelp = false;
    while (1) {
        if (!ignoreHelp) {
            printf("Welcome to my cool calculator!\nWhich operation do you want to use?\n"
                "  + to add\n"
                "  - to subtract\n"
                "  * to multiply\n"
                "  q to exit\n");
        }

        fgets(s, 2000, stdin);
        int len = strlen(s);
        if (len <= 1) {
            ignoreHelp = true;
            continue;
        }
        
        switch (s[0]) {
            case '+':
                addPrompt();
                break;
            case '-':
                subPrompt();
                break;
            case '*':
                mulPrompt();
                break;
            case 'q':
                return;
        }
    }
}

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
	gid_t gid = getegid();
	setresgid(gid, gid, gid);

    pwn();

    return 0;
}