#ifndef DATA_STRUCTURES_H
#define DATA_STRUCTURES_H

typedef struct NodeLetterCount
{
    char c;
    int count;

    struct NodeLetterCount* prev;
    struct NodeLetterCount* next;
} NodeLetterCount;

typedef struct Node
{
    NodeLetterCount* firstLetterCount;
} Node;

void HelloFromData();
#endif