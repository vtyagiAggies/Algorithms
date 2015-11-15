#include<stdio.h>

void reverse(char* string){
  char* end = string;
  char temp;
  printf("I am here");
  while(*end){
    ++end;
  }
  printf("I am here");
  --end; //To ignore last characer because its a null charcater
  while(string < end){
     temp = *string;
     *string = *end;
     *end = temp;
     end--;
     string++;
  }
}

int main()
 {
    char str[]  = "Hello";
    printf("I am here 24");
    reverse(str);
    printf("Answer: %s\n",str);
    return 0;
 }
