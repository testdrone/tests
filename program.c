#include <stdio.h>
#include <string.h>

int main() {
  char s[20], int i;
  printf("Enter your name:\t");
  fgets(s, 20, stdin);
  printf("Your name is %s\n", s);
  printf("End can be %c \n", s[14]/*s[strlen(s) - 1]*/);
  //This is to test the patch file.
  return 0;
}
