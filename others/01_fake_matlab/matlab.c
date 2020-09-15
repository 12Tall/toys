#include <stdlib.h>
#include <stdio.h>

int main()
{
    char *dir = getenv("MATLAB");
    if (dir != NULL)
    {
        printf("%%MATLAB%%: %s\n", getenv("MATLAB"));
        system("%MATLAB%\\matlab.bat");
    }
    else
    {
        printf("Environment 'MATLAB' not found\n", getenv("MATLAB"));
        exit(1);
    }
    exit(0);
}