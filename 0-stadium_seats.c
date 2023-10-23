#include <stdio.h>

int main(int argc, int *argv){
    if(argc!=2){
        printf("Usage: ./stadium_seats row\n");
        return 0;
    }
    int i = argv[1];
    stadium_seats(i);

    return 0;
}

int stadium_seats(row)
int row;
{
    for(int i=row; i>=1; i--){
        for(int j=1; j<=i; j++){
            putchar("*");
        }
        putchar("\n");
    }
    return 0;
}