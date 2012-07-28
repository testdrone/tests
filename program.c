#include <stdio.h>
#include <string.h>

int main() {
  char s[20];
  printf("Enter your name:\t");
  fgets(s, 20, stdin);
  printf("Your name is %s\n", s);
  printf("End is %c \n", s[14]/*s[strlen(s) - 1]*/);
  return 0;
}
