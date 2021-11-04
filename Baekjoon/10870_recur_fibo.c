#include <stdio.h>

int main(){
    int number;
    scanf("%d", &number);
    int result = fib(number);
    printf("%d", result);
}

int fib(int n){
    if (n == 0) return 0;
    if (n == 1) return 1;
    return (fib(n-1)+ fib(n-2));
}