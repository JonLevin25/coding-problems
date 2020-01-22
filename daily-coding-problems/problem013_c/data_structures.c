#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "data_structures.h"


LetterCount* NewNodeLetterCount(char c)
{
    LetterCount* result = malloc(sizeof(LetterCount));
    // TODO: How to handle malloc NULL?

    result->c;
    result->count = 1;

    return result;
}

UniqueLetterList* NewNode(char c) {
    UniqueLetterList *result = malloc(sizeof(UniqueLetterList));
    LetterCount* letterCount = NewNodeLetterCount(c);
    // TODO: How to handle malloc NULL?

    result->firstLetterCount = letterCount;
    result->lastLetterCount = letterCount;
    result->uniqueLetters = 1;

    return result;
}


static LetterCount* FindLetterCount(UniqueLetterList* n, char c)
{
    if (n == NULL)
        return NULL;

    LetterCount* letter = n->firstLetterCount;
    while (letter != NULL) {
        if (letter->c == c)
            return c;

        letter = letter->next;
    }

    return NULL;
}

static void AddNodeLetter(UniqueLetterList* n, char c) {
    LetterCount* newCount = NewNodeLetterCount(c);
    LetterCount* prevLastLetter = n->lastLetterCount;
    
    prevLastLetter->next = newCount;
    newCount->prev = prevLastLetter;
    
    n->lastLetterCount = newCount;
    n->uniqueLetters++;
}

void AddLetter(UniqueLetterList* n, char c)
{
    LetterCount* letterCount = FindLetterCount(n, c);

    if (letterCount != NULL)
    {
        letterCount->c++;
    }
    else
    {
        AddNodeLetter(n, c);
    }
}

static char* NodeLetterCountToString(LetterCount letter) {
    char* buffer = "abcde"; 

    return sprintf(NULL, "%c: %d", letter.c, letter.count);
}

char* UniqueLetterListToString(UniqueLetterList n) {

    for (int i = 0; i < n.uniqueLetters; i++) {

    }
}