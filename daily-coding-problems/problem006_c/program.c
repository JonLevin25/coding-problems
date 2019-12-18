#include <stdio.h>
#include <assert.h>

void test();

int main(){
    test();
    return 0;
}

// TODO: extract tests to separate file + automate compilation to task in vscode
// TODO: learn more about c module linking/including for this
void test(){
    printf("Hello world!\n");
}
