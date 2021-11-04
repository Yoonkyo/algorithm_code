#include <stdio.h>

int main(){
    int number;
    scanf("%d", &number);
    int result = factorial(number);
    printf("%d", result);
}

int factorial(int n){
    if (n <= 1){
        return 1;
    }
    else{
        return n*factorial(n-1);
    }
}