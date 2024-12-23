#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to convert hex string to bytes
void hexStringToBytes(const char *hexStr, char *bytes, size_t bytesLen) {
  for (size_t i = 0; i < bytesLen; i++) {
    sscanf(hexStr + 2 * i, "%2hhx", &bytes[i]);
  }
}

// Function to shuffle the array in reverse order
void reverseShuffle(char *array, size_t n) {
  if (n > 1) {
    srand(55353600); // Same seed as used in transformation
    size_t i;
    for (i = n - 1; i > 0; i--) {
      size_t j = i + rand() / (RAND_MAX / (n - i) + 1);
      char t = array[j];
      array[j] = array[i];
      array[i] = t;
    }
  }
}

void reverseTransform(const char *transformedStr) {
  size_t len = strlen(transformedStr) / 2;
  char *bytes = (char *)malloc(len); // Corrected line

  hexStringToBytes(transformedStr, bytes, len);

  // Reverse XOR with 15 and shuffle
  for (size_t i = 0; i < len; i++) {
    bytes[i] ^= 15;
  }
  reverseShuffle(bytes, len);

  // Reverse XOR with 10
  for (size_t i = 0; i < len; i++) {
    bytes[i] ^= 10;
    printf("%c", bytes[i]);
  }

  free(bytes);
}

int main() {
  // The transformed log file content (example, truncated)
  const char *logFileContent =
      "6b607d7168646c6b71606b646b66606475756a6c6b7168606b717760736c6072686a716a"
      "77667c66696068646b7064696d647769607c6164736c61766a6b666a6b73606b716c6a6b"
      "67666d6c75053705676c6e60776c6160772b666a687272722b646a692b666a6867666d6c"
      "750546056d6c7576055505647676726a7761343736316d607c666d70666e296d6a727c64"
      "616a6c6b052a057c6a706e6060756c6b716d60777067676077766c6160616a726b052a05"
      "6c72646b716061716a64766e7c6a70726d6077607c6a70626a717c6a70776d647769607c"
      "2b6260716764666e716a6860647664752b6760767129676477777c2b726d64716c763105"
      "38053d7272722b7c646d6a6a2b666a687272722b68766b2b666a686d6a72716a70766060"
      "7d666069766d6a7771667071716a66696a7660726c6b616a72"; // Replace with
                                                            // actual content

  reverseTransform(logFileContent);

  return 0;
}
