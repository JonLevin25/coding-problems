#include <stdlib.h>
#include <stdio.h>
#include "data_structures.h"


void HelloFromData() {
    printf("HelloFromData!");
}

NodeLetterCount* NewNodeLetterCount(char c)
{
    NodeLetterCount* result = malloc(sizeof(NodeLetterCount));
    result->c;
    result->count = 1;

    return result;
}

Node* NewNode(char c) {
    Node *result = malloc(sizeof(Node));
    NodeLetterCount* letterCount = NewNodeLetterCount(c);
    result->firstLetterCount = letterCount;

    return result;
}

NodeLetterCount* FindLetterCount(Node* n, char c)
{
    if (n == NULL)
        return NULL;

    NodeLetterCount* letter = n->firstLetterCount;
    while (letter != NULL) {
        if (letter->c == c)
            return c;

        letter = letter->next;
    }

    return NULL;
}

void AddLetter(Node* n, char c)
{
    NodeLetterCount* letterCount = FindLetterCount(n, c);

    if (letterCount != NULL)
    {
        letterCount->c++;
    }
    else
    {
        // TODO: handle adding letter
        // TODO: How to handle malloc NULL?
        
    }
}
