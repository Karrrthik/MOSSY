#include <stdio.h>

int main(){
    int a, b, answer = 0, LCF;
    scanf("%d %d", &a, &b);
    // this is here to change a set where a and b are both negative to change them to positive. 
    if (a < 0 && b < 0){
        a *= -1;
        b *= -1;
    }
    // determine which of the two a, b is largest
    int greatest = (a <= b) ? b : a;
    // find the largest common factor
    for (int i = 1; i < greatest/2; i++){
        if (a%i == 0 && b%i == 0)
            LCF = i;
    }
    // if a*b is greater than zero then multiply both and devide by the LCF and if it is negative, do the same but multiply by -1 to make it positive.
    answer = (a*b > 0) ? (a * b) / LCF : -1 * ((a * b) / LCF);
    // in the case that a and b are both zero then keep the anwer as 0.
    if (a == 0 || b == 0)
        answer = 0;

    printf("%d\n", answer);
    return 0;
}