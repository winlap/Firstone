#include <stdio.h>
#include <string.h>

#define MAX_PARAGRAPH_LENGTH 1000
#define MAX_WORD_LENGTH 50

int main() {
    char paragraph[MAX_PARAGRAPH_LENGTH];
    char word[MAX_WORD_LENGTH];
    int word_count = 0;

    printf("Enter a paragraph of text:\n");
    fgets(paragraph, MAX_PARAGRAPH_LENGTH, stdin);

    printf("Enter a word to count:\n");
    scanf("%s", word);

    // Remove the newline character from the end of the paragraph
    paragraph[strcspn(paragraph, "\n")] = '\0';

    // Tokenize the paragraph into individual words
    char *token = strtok(paragraph, " ");
    while (token != NULL) {
        if (strcmp(token, word) == 0) {
            word_count++;
        }
        token = strtok(NULL, " ");
    }

    printf("The word '%s' appears %d times in the paragraph.\n", word, word_count);

    return 0;
}

