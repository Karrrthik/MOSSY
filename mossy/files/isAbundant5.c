#include <stdio.h>

int main(){
    int n, answer = 0;
    scanf("%d", &n);

    // keep the number positive
    n = (n < 0) ? n * -1 : n;
    // find how many numbers divide n and if there is no remainder add 1 to answer
    for (int i = 1; i < n; i++){
        if (n % i == 0)
            answer += i;
    }
    
    // print the respective answer accordingly to "answer"
    if (answer < n)
        printf("Deficient\n");

    if (answer == n)
        printf("Perfect\n");

    if (answer > n)
        printf("Abundant\n");
    return 0;
}