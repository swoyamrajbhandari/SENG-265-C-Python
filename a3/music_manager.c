/** @file music_manager.c
 *  @brief A small program to analyze songs data.
 *  @author Mike Z.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Jose O.
 *  @author Victoria L.
 *  @author Swoyam Rajbhandari
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

#define MAX_LINE_LEN 200

node_t* file_parse(FILE* filename, int sort_col);                 //function declarations.
FILE* open_file(char* filename);
FILE* output_file(char* filename);
void output_data(FILE* outputFile, node_t* list ,char* display);

/**
 * @brief Serves as an incremental counter for navigating the list.
 *
 * @param p The pointer of the node to print.
 * @param arg The pointer of the index.
 *
 */
void inccounter(node_t *p, void *arg)
{
    int *ip = (int *)arg;
    (*ip)++;
}

/**
 * @brief Allows to print out the content of a node.
 *
 * @param p The pointer of the node to print.
 * @param arg The format of the string.
 *
 */
void print_node(node_t *p, void *arg)
{
    char *fmt = (char *)arg;
    printf(fmt, p->sortby);

}

/**
 * @brief Allows to print each node in the list.
 *
 * @param l The first node in the list
 *
 */
void analysis(node_t *l)
{
    int len = 0;

    apply(l, inccounter, &len);
    printf("Number of words: %d\n", len);

    apply(l, print_node, "%s\n");
}

/**
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */
int main(int argc, char *argv[]) {

    char sort_by[20];
    char display[20];
    char filename[100];

    if (argc < 4) {
        return 1;
    }

    sscanf(argv[1], "--sortBy=%19s", sort_by);    //processing argument values.
    sscanf(argv[2], "--display=%19s", display);
    sscanf(argv[3], "--files=%99s", filename); 
    
    int sort_col;
    if (strcmp(sort_by, "popularity") == 0 ){
        sort_col = 6;

    } else if (strcmp(sort_by, "danceability") == 0 ){
        sort_col = 7;
    } else if (strcmp(sort_by, "energy") == 0 ){
        sort_col = 8;
    }

    FILE* file = open_file(filename);                //open input file.

    node_t* list = file_parse(file, sort_col);       //parse passed input file.

    FILE* outputFile = output_file("output.csv");    //open output file.

    output_data(outputFile, list, display);

    // Releasing the space allocated for the list and other emalloc'ed elements
    node_t *temp_n = NULL;
    for (; list != NULL; list = temp_n)
    {
        temp_n = list->next;
        free(list->artist);
        free(list->song);
        free(list->year);
        free(list->sortby);

        free(list);
    }

    fclose(outputFile);
    fclose(file);

    exit(0);
}

/**
 * @brief Parses the given file and creates a linked list of ordered nodes.
 * 
 * @param filename The file pointer to the input file.
 * @param sort_col The column number used for sorting file data.
 * @return node_t* A pointer to the head of the created linked list.
 *
 */

node_t* file_parse(FILE* filename, int sort_col){

    char *line = NULL;
    char *token;
    node_t *list = NULL;
    line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);

    char* artist = NULL;
    char* song = NULL;
    char* year = NULL;
    char* sortby = NULL;

    while (fgets(line, MAX_LINE_LEN, filename) != NULL){

        int column = 1;
        token = strtok(line, ",");

        while (token != NULL){
            if (column == 1){                   //artist column.
                artist = strdup(token);

            } else if (column == 2){           //song column.
                song = strdup(token);

            }  else if (column == 5){         //year column.
                year = strdup(token);

            } else if (column == sort_col){    //sortby value column.
                sortby = strdup(token);
            }

            token = strtok(NULL, ",");
            column++;
                
        }

        list = add_inorder(list, new_node(artist, song, year, sortby));
    }

    free(line);
    return list;
}

/**
 * @brief Opens a file for reading and returns a file pointer.
 * 
 * @param filename The name of the file to be opened.
 * @return FILE* A file pointer to the opened file, or NULL if an error occurs. 
 *
 */

FILE* open_file(char* filename){
    
    FILE* file = fopen(filename, "r");

    if (file == NULL) {                           //error if the passed file fails to open
        printf("Error in opening file\n");

    }

    return file;

}

/**
 * @brief Opens an output file for writing and returns a file pointer.
 * 
 * @param filename The name of the output file to be opened.
 * @return FILE* A file pointer to the opened output file, or NULL if an error occurs. 
 *
 */

FILE* output_file(char* filename){
    
    FILE* outputFile = fopen("output.csv", "w");

    if (outputFile == NULL) {
        printf("Error opening output file\n");          //error if the passed file fails to open
    }

    return outputFile;
}

/**
 * @brief Outputs data from linked list to the output file.
 * 
 * @param outputFile A file pointer to the output file.
 * @param list A pointer to the head of the linked list.
 * @param display The display value indicating the number of records to write from the linked list.
 * @return void 
 *
 */

void output_data(FILE* outputFile, node_t* list ,char* display){

    node_t* curr = list;
    int count = 0;
   
    while (curr != NULL && count <= atoi(display)) {
        fprintf(outputFile, "%s,%s,%s,%s\n", curr->artist, curr->song, curr->year, curr->sortby );
        curr = curr->next;
        count++;
    }
    
}


