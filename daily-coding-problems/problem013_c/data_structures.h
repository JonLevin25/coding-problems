#ifndef DATA_STRUCTURES_H
#define DATA_STRUCTURES_H

typedef struct LetterCount
{
    char c;
    int count;

    struct LetterCount* prev;
    struct LetterCount* next;
} LetterCount;

typedef struct UniqueLetterList
{
    LetterCount* firstLetterCount;
    LetterCount* lastLetterCount;
    int uniqueLetters;
    
    UniqueLetterList* next;
    UniqueLetterList* prev;
} UniqueLetterList;

typedef struct LinkedListNode {
    LinkedListNode* prev;
    LinkedListNode* next;
    void* value;
} LinkedListNode;

UniqueLetterList* NewNode(char c);

void AddLetter(UniqueLetterList* n, char c);

char* UniqueLetterListToString(UniqueLetterList n);

#endif