#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct XorLinkedNode {
    int both;
    int value;
} XorLinkedNode;

typedef struct XorLinkedList{
    XorLinkedNode *first;
    XorLinkedNode *last;
} XorLinkedList;

void add(XorLinkedList *list, int value){
    XorLinkedNode *newNode = malloc(sizeof(XorLinkedNode));
    newNode->value = value;
    newNode->both = 0;

    if (list->first == NULL){
        list->first = newNode;
        list->last = newNode;
        return;
    }

    // Set list last ref
    XorLinkedNode *prevNode = list->last;
    list->last = newNode;

    // Update XOR ref
    int prevBoth = prevNode->both;
    int newPrevBoth = prevBoth ^ (int)newNode;
    prevNode->both = newPrevBoth; // prevNode.both should already contain previous node value, XOR it with next (newNode)
    newNode->both = (int) prevNode;
}

int get(XorLinkedList *list, int index){
    XorLinkedNode *currNode = list->first;
    XorLinkedNode *prevNode = NULL;
    for (int i = 0; i < index; i++){
        XorLinkedNode *nextNode = (XorLinkedNode *)(currNode->both ^ (int)prevNode);
        prevNode = currNode;
        currNode = nextNode;
    }

    return currNode->value;
}

void printVal(XorLinkedList *list, int i){
    printf("list[%i] = %i\n", i, get(list, i));
}

int main(){
    XorLinkedList *list = malloc(sizeof(XorLinkedList));
    list->first = NULL;
    list->last = NULL;

    add(list, 10);
    add(list, 11);
    add(list, 12);

    printVal(list, 0);
    printVal(list, 1);
    printVal(list, 2);
}

// TODO: extract tests to separate file + automate compilation to task in vscode
// TODO: learn more about c module linking/including for this
void test(){
    XorLinkedNode *test = malloc(sizeof(XorLinkedNode));
    test->both = 3;
    printf("%d", test->both);
}
