#include <stdlib.h>
#include <stdio.h>

/* sets bits i through j in tgt to match src */
void setBits(int *tgt, int src, short i, short j) {
    int mask = (((int)pow(2, j - i + 1)) - 1) << i;
    *tgt = (src & mask) | (*tgt & ~mask);
}

#include <math.h>

/* prints the given number in binary into the given buffer */
char* printBinary(int num, char* buffer) {
    for(int i = 0; i < sizeof(num) * 4; i++) {
        if(num & 1) {
            buffer[i] = '1';
        } else {
            buffer[i] = '0';
        }
        num >>= 1;
    }
    buffer[sizeof(num) * 4] = '\0';
    return buffer;
}

/* print each step of an example problem for debugging */
void printExample(int *tgt, int src, short i, short j) {
    int mask = (((int)pow(2, j - i + 1)) - 1) << i;
    char buffer[33];
    printf("src & mask:\n");
    printf("  %s\n", printBinary(src, buffer));
    printf("& %s\n", printBinary(mask, buffer));
    printf("--------------------------------\n");
    printf("  %s\n\n", printBinary(src & mask, buffer));

    printf("*tgt & !mask:\n");
    printf("  %s\n", printBinary(*tgt, buffer));
    printf("& %s\n", printBinary(~mask, buffer));
    printf("--------------------------------\n");
    printf("  %s\n\n", printBinary(*tgt & !mask, buffer));
    
    printf("x | y:\n");
    printf("  %s\n", printBinary(src & mask, buffer));
    printf("| %s\n", printBinary(*tgt & ~mask, buffer));
    printf("--------------------------------\n");
    printf("  %s\n\n", printBinary((src & mask) | (*tgt & ~mask), buffer));
}

void runTest(int expected, int tgt, int src, short i, short j) {
    setBits(&tgt, src, i, j);
    if(tgt != expected) {
        printf("Error: expected %d got %d.\n", expected, tgt);
    }
}

int main() {
    runTest(0, 1, 0, 0, 1);
    runTest(0, 47, 0, 0, 31);
    runTest(3, 3, 0, 2, 7);
    printf("Ran all tests!\n");
}

/*
  0000000000000000
& 0000000011111100
  0000000000000000

  0000000000000011
& 1111111100000011
  0000000000000011

  0000000000000000
| 0000000000000011
  0000000000000011

  mask = 4+8+16+32+64+128 = 252
*/
