#include <stdio.h>

/**
*create_tensor: create a 1D array to hold a tensor (tensor in TensorFlow)
* @x: no. of px on x co-ord
*@y: no. of px on y co-ord
*@dim: no. of dimensions (or, how many 2D arrays there are)
*return: addr of said mem space
*/

int create_tensor(int *x, int *y, int *dim){
    int px = &x * &y * &dim;
    int *size [] = malloc(sizeof(int) * px);

    if (size == NULL) {
        return 1;
    }

    return size;
}

int traverse_tensor(int offset, int stride){
    int idx = (&x * stride)  - offset;
    return &size[idx];
}