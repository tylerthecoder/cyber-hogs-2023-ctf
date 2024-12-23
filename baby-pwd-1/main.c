#include <time.h>
#include <stdio.h>
#include <stdlib.h>

void pwn() {
    srand(time(NULL));
    
    char s[20];
    long long randomNumber;
    long long inputNumber;
    
    randomNumber = ((long long)rand() << 32) | rand();
    fgets(s, 50, stdin);
    inputNumber = strtoll(s, NULL, 10);
    
    if (randomNumber == inputNumber) {
        printf("Congrats! The correct number was %lld!\n", randomNumber);
        system("cat flag.txt");
    } else {
        printf("Sorry, the correct number was %lld, not %lld.\n", randomNumber, inputNumber);
        printf("Better luck next time!\n");
    }
}

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    printf("Guess a number: ");
    pwn();

    return 0;
}