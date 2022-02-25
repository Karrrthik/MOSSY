#include <stdio.h>

int main(){
// for every new line, we print @ if the variable j is in between the necessary positions. I do I repeat it twice instead of 
// doing it simultaneously because it is easier to understand
for (int i = 0; i <= 9; i++){
    for (int k = 0; k <= 1; k++){
        for (int j = 0; j < 22; j++){
            if (j >= 10 - i && j <= 10 + i + 1)
                printf("@");
            else    
                printf("$");
        }
    }
printf("\n");
}

// this is just the inverse of the first set of loops minus the last line which is why i starts at 8 and not 9.
for (int i = 8; i >= 0; i--){
    for (int k = 0; k <= 1; k++){
        for (int j = 0; j < 22; j++){
            if (j >= 10 - i && j <= 10 + i + 1)
                printf("@");
            else    
                printf("$");
        }
    }
printf("\n");
}


    return 0;
}