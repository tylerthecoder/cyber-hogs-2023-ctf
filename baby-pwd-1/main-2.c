#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);

  srand(time(NULL));

  char s[20];
  long long randomNumber;
  long long inputNumber;

  randomNumber = ((long long)rand() << 32) | rand();

  // print the random number to the screen
  printf("%lld\n", randomNumber);
}
