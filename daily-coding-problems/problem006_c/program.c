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

void add(XorLinkedList list, int value){
    XorLinkedNode *newNode = malloc(sizeof(XorLinkedNode));
    if (list.first == NULL){
        list.first = newNode;
        list.last = newNode;
        return;
    }

    XorLinkedNode *prevNode = list.last;
    list.last = newNode;
    prevNode->both ^= (int)newNode; // prevNode.both should already contain previous node value, XOR it with next (newNode)
    newNode->both = (int) prevNode;
}

int get(XorLinkedList *list, int index){
    XorLinkedNode *currNode = list->first;
    XorLinkedNode *prevNode = NULL;
    for (int i = 0; i < index; i++){ // TODO: ObO?
        currNode = currNode->both ^ (int)prevNode;
    }

    return currNode->value;
}

void testWithValue(XorLinkedNode node, int newValue){
    node.value = newValue;
}

void testWithPointer(XorLinkedNode *node, int newValue){
    node->value = newValue;
}

int main(){
    XorLinkedNode *node = malloc(sizeof(XorLinkedNode));
    node->value = 1;
    printf("%d", node->value);
    return 0;
}

// TODO: extract tests to separate file + automate compilation to task in vscode
// TODO: learn more about c module linking/including for this
void test(){
    XorLinkedNode *test = malloc(sizeof(XorLinkedNode));
    test->both = 3;
    printf("%d", test->both);
}
