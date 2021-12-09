#include <stdio.h>

/**
* ack - the ackerman problem
* @m: arg 1
* @n:  arg 2
* Return: the solution to ackerman's problem
*
*/

int ack(int m, int n)
{
int ans;
if (m == 0) ans = n + 1;
else if (n == 0) ans = ack(m - 1, 1);
else ans = ack(m - 1, ack(m, n - 1));
return ans;
}

int main(int __attribute__((__unused__)) argc, char __attribute__((__unused__)) **argv){
int i, j;
for (i = 0; i < 6; i++)
for (j = 0; j <6; j++)
printf("ackerman (%d, %d) is: %d\n", i, j, ack(i, j));
}
