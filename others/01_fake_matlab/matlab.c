#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define MAX_PATH 1024
int main(int argc, char *argv[])
{
    char params[MAX_PATH] = {0};

    char *dir = getenv("MATLAB");
    if (dir != NULL)
    {
        printf("%%MATLAB%%: %s\n", getenv("MATLAB"));
        strcpy(params, "%MATLAB%\\matlab.bat ");
        for (int i = 1; i < argc; i++)
        {
            strcat(params, "\"");
            strcat(params, argv[i]);
            strcat(params, "\" ");
        }

        printf("run: %s \n", params);

        system(params);
    }
    else
    {
        printf("Environment 'MATLAB' not found\n", getenv("MATLAB"));
        exit(1);
    }
    exit(0);
}