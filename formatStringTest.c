#include <stdio.h>

int loggedIn = 0;
char secret[] = "This is my super secret string!";

int main() {
  char f[512];
  char *ptr = secret;
  
  printf("Input a format string: ");
  
  fgets(f, sizeof(f), stdin);

  printf(f);

  printf("\n");
  
  printf("\nLogged in = %d\n",loggedIn);

  if (loggedIn) {
    printf("Yay! You logged in!\n");
  }
  else {
    printf("You aren't logged in :(\n");
  }

}

