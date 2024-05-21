#include <stdio.h>
#include <stdlib.h>

int stadium_seats(row)
int row;
{
    for(int i=row; i>0; i--){
        for(int j=0; j<i; j++){
            putchar('*');
        }
        putchar('\n');
    }
    return 0;
}

int main(int argc, char *argv[]){
    if(argc!=2){
        printf("Usage: ./stadium_seats n_row\n");
        return 0;
    }
    int i =  atoi(argv[1]);
    stadium_seats(i);
    
    return 0;
}


/**
stadium_seats(5)

*****
****
***
**
*


*/