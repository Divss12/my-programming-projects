#include <stdio.h>

int main() {
    int a = 2;
    int b = 2;
    int c = 2;
    int matrixA[a][b];
    int matrixB[b][c];
    int matrixC[a][c];

    matrixA[0][0] = 1;
    matrixA[0][1] = 2;
    matrixA[1][0] = 3;
    matrixA[1][1] = 4;

    matrixB[0][0] = 5;
    matrixB[0][1] = 6;
    matrixB[1][0] = 7;
    matrixB[1][1] = 8;

/*    
    for (int i = 0; i < a; i++){
        for (int j = 0; j < b; j++){
            printf("Matrix A pos (%d,%d): ",i,j);
            matrixA[i][j] = getchar(void);
        }
    }

    for (int p = 0; p < a; p++){
        for (int q = 0; q < b; q++){
            printf("Matrix B pos (%d,%d):",p,q);
            matrixA[p][q] = getchar(void);
        }
    }
*/
    for (int x = 0; x < a; x++){
        for (int y = 0; y < c; y++){
            matrixC[x][y] = 0;
            for (int z = 0; z < b; z++){
                matrixC[x][y] += matrixA[x][z] * matrixB[z][y];
            }
        }
    }

    for (int p = 0; p < a; p++){
        for (int q = 0; q < c; q++){
            printf("%d  ",matrixC[p][q]);
        }
        printf("\n");
    }
}