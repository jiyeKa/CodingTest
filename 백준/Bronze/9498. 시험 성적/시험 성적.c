#define _CRT_SECURE_NO_WARNNINGS
#include <stdio.h>

int main(void){
    int score;
    int val;
    scanf("%d",&score);
    val = score / 10;
  
    switch(val){
        case 10:
        case 9:
            printf("A");
            break;
        case 8:
            printf("B");
            break;
        case 7:
            printf("C");
            break;
        case 6:
            printf("D");
            break;
        default:
            printf("F");
    }

    return 0;
}
