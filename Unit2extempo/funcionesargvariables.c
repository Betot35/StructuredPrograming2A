#include <stdio.h>
#include "headerPractice.h"
#include <stdlib.h>

int var1 = 10;
int var2 = 20;

int main (int argc, char**  argv){
    printf(" Just maini: var1 = %d, var2 = %d \n", var1, var2);
    printf("Function was executed:\n");
    //paso de argumentos por dirección//
    modifyVariables(var1, var2);
    printf(" var1 = %d, var2 = %d \n", var1, var2);


    //Get the address of var1 and var2//
    //& = La dirección de// --> &x00879fb
    int * myptr1 = &var1;

    ShowAddress(myptr1);
    ShowAddress(myptr2); 

    int * myptr2 = &var2;
    printf("address var1: %p, \t address var2: %p \n", myptr1, myptr2);

    printf("Pointer has been modified the var1: \n");
    //*myptr1 = El valor de// --> &x00879fb = x;
    myptr1 = &var1;
    *myptr1 = 20;
    var2 = 40; 



    printf("///Pointers into functions///\n");
    printf(" var1 = %d, var2 = %d \n", var1, var2);

    //printf("Function address was executed:\n");
    //Paso de argumentos por dirección//
    modifyVariablesAddress(&var1, &var2);

    //printf(" var1 = %d, var2 = %d \n", var1, var2);

    return 0;
}