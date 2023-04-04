int lengthOfString(char* str) {
    char* pEnd = str;
    while (*pEnd) pEnd++;
    return (int) (pEnd - str);
}

void copyString(char* to, char* from) {
    while (*from) *to++ = *from++;
    *to = '\0';
}