#include <stdio.h>
#include <stdlib.h>

struct Elem
{
    struct Elem *prev, *next;
    int v;
};

void InsertAfter(struct Elem *first, struct Elem *second)
{
    struct Elem *third;
    third = first->next;
    first->next = second;

    second->prev = first;
    second->next = third;

    third->prev = second;
}

void Delete(struct Elem *actual)
{
    struct Elem *second, *third;

    second = actual->prev;
    third = actual->next;

    second->next = third;
    third->prev = second;

    actual->prev = NULL;
    actual->next = NULL;
}

struct Elem *find_loc(struct Elem *head, struct Elem *ind)
{
    struct Elem *helper = ind->prev;

    while (helper != head && helper->v > ind->v)
        helper = helper->prev;

    return helper;
}

void InsentionSort(struct Elem *head, int n)
{
    struct Elem *i, *ind, *loc;
    ind = head->next;

    for (int k = 0; k < n; k++)
    {
        loc = find_loc(head, ind);
        ind = ind->next;
        i = ind->prev;
        Delete(i);
        InsertAfter(loc, i);
    }
}

int main()
{
    int n;
    scanf("%d", &n);

    struct Elem *elem;
    struct Elem *head = (struct Elem *)malloc(sizeof(struct Elem));
    head->next = head;
    head->prev = head;

    for (int i = 0; i < n; i++)
    {
        elem = (struct Elem *)malloc(sizeof(struct Elem));
        scanf("%d", &(elem->v));
        InsertAfter(head, elem);
    }

    InsentionSort(head, n);

    elem = head->next;
    while (elem != head)
    {
        printf("%d ", elem->v);
        elem = elem->next;
    }

    elem = head->next;
    while (elem != head)
    {
        struct Elem *prev = elem;
        elem = elem->next;
        free(prev);
    }
    free(head);

    return 0;
}