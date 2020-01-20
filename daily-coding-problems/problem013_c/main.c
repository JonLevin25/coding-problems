#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct NodeLetterCount
{
    char c;
    int count;
} NodeLetterCount;

typedef struct Node
{
    NodeLetterCount letterCounts[];

} Node;

void AddLetter(Node* n, char c) {
    
    NodeLetterCount letterCounts[] = n->letterCounts;
    int l = sizeof(letterCounts) / sizeof(NodeLetterCount);

    bool found = false;
    for (int i = 0; i < l; i++) {
        NodeLetterCount letterCount = letterCounts[i];
        if (letterCount.c == c) {
            letterCount.count++;
            found = true;
        }
    }

    if (found) return;

}

// TODO: extract tests to separate file + automate compilation to task in vscode
// TODO: learn more about c module linking/including for this
void test1(){
    
}

int main(){
    test1();
    return 0;
}