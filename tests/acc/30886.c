#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void concat(const char *s1, const char *s2, char* c)
{
    char *t = "#";
    strcpy(c, s1);
    strcat(c, t);
    strcat(c, s2);
}


int *prefix_f(char *s) {
    int len = strlen(s);
    int *res = malloc(len * sizeof(int));
    for (int i = 0; i < len; i++) {
        res[i] = 0;
    }
    for (int i = 1; i < len; i++) {
        int t = res[i - 1];
        while (t > 0 && s[i] != s[t]) {
            t = res[t - 1];
        }
        if (s[i] == s[t]) {
            t++;
        }
        res[i] = t;
    }
    return res;
}


int main(int argc, char *argv[]) {
    char *a = argv[1];
    char *b = argv[2];
    int len_a = strlen(a);
    int len_b = strlen(b);
    char c[len_a+len_b+2];
    concat(a, b, c);
    int *pref_c = prefix_f(c);
    int i = strlen(c)-1;
    while( i > len_a){
        if (pref_c[i] > 0){
            i = i - pref_c[i];
        }else{
            printf("no");
            free(pref_c);
            return 0;
        }
    }
    
    printf("yes");
    free(pref_c);
    return 0;
}
