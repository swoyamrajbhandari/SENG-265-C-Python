/** @file event_manager.c
 *  @brief A pipes & filters program that uses conditionals, loops, and string processing tools in C to process iCalendar
 *  events and printing them in a user-friendly format.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Jose O.
 *  @author Victoria L.
 *  @author Swoyam Rajbhandari
 *
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * @brief The maximum line length.
 *
 */
#define MAX_LINE_LEN 132

/**
 * @brief The structures used to store variables related to argument, file and previous date data.
 * 
*/

typedef struct {                  //argument start and end date data         
    int arg_syear;
    int arg_smonth;
    int arg_sday;
    int arg_eyear;
    int arg_emonth;
    int arg_eday;
} Arg;

typedef struct {                     //file event data.
    char start_year[5];
    char start_month[3];
    char start_day[3];
    char start_hour[3];
    char start_min[3];
    char end_year[5];
    char end_month[3];
    char end_day[3];
    char end_hour[3];
    char end_min[3];
    char location[101];
    char summary[101];
} Event;

typedef struct {                  //previous file event data
    char prev_year[5];
    char prev_month[3];
    char prev_day[3];
} PrevDate;

/**
 * @brief Explicit declaration of all the functions used in the program.
 * 
*/

void arg_process(char* start, char* end, Arg* arg);
void get_file_data(FILE* file, Event *event,  Arg* arg, PrevDate* prev);
void print_repeat(Event* event, char* untill , PrevDate* prev);
int within_range(Event* event, Arg* arg);
const char* month_name(char* month);
char* convertTo12HourFormat(char* hour, char* min, char* conv_hour);
void print_output(Event *event, PrevDate* prev);
void print_dash(const char* count);

/**
 * Function: main
 * --------------
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */

int main(int argc, char *argv[]) {

    char start_date[20];
    char end_date[20];
    char filename[100];

    if (argc < 4) {
        return 1;
    }

    sscanf(argv[1], "--start=%19s", start_date);    //processing argument values.
    sscanf(argv[2], "--end=%19s", end_date);
    sscanf(argv[3], "--file=%99s", filename); 

    FILE* file = fopen(filename, "r");

    if (file == NULL) {                           //error if the passed file fails to open
        printf("Error in opening file\n");
        return 1;
    }

    Event event;                                  //declaring variables for the structs.
    Arg arg;
    PrevDate prev;

    arg_process(start_date, end_date, &arg);
    get_file_data(file, &event, &arg, &prev);

    fclose(file);

    exit(0);
}

/**
 * Function: arg_process
 * ---------------------
 * @brief The arg_process extracts and stores the start and end date values from the 
 *         command line arguments in variables from the Arg struct. 
 * @param start The start date value passed from main.
 * @param end The end date value passed from main.
 * 
 */

void arg_process(char* start, char* end, Arg* arg){

    sscanf(start, "%d/%d/%d", &arg->arg_syear, &arg->arg_smonth, &arg->arg_sday);      //processing start date argument

    sscanf(end, "%d/%d/%d", &arg->arg_eyear, &arg->arg_emonth, &arg->arg_eday);       //processing end date argument

}

/**
 * Function: within_range
 * ----------------------
 * @brief The within_range function returns 0 if the passed file event falls within 
 *        the argument start and end date range.
 * @param event A pointer to the Event struct variable representing the event.
 * @param arg A pointer to the Arg struct variable containing the start and end date range.
 * @return int: 0 if the event falls within the date range, and 1 otherwise.
 *
 */

int within_range(Event* event,Arg* arg){

    int file_year, file_month, file_day;                     //storing string-format file date as integers.
    sscanf(event->start_year, "%d", &file_year);
    sscanf(event->start_month, "%d", &file_month);
    sscanf(event->start_day, "%d", &file_day);

    if (file_year > arg->arg_eyear || file_year < arg->arg_syear) {                //comparing file start date with argument start and end range.
        return 1;
    }
    else if ((file_year == arg->arg_syear) && (file_month < arg->arg_smonth || (file_month == arg->arg_smonth && file_day < arg->arg_sday))) {
        return 1;
    }
    else if ((file_year == arg->arg_eyear) && (file_month > arg->arg_emonth || (file_month == arg->arg_emonth && file_day > arg->arg_eday))) {
        return 1;
    }
    return 0;

}

/**
 * Function: get_file_data
 * -----------------------
 * @brief The get_file_data function reads data from the provided file and extracts relevant information for each event.
 *        It then checks if each event falls within the specified date range (using within_range function),
 *        and based on the result, either prints the event information or handles recurring events.
 * @param file A pointer to the file from which data is being read.
 * @param event A pointer to the Event struct variable for storing event information.
 * @param arg A pointer to the Arg struct variable representing the date range.
 * @param prev A pointer to the PrevDate struct variable for handling recurring events.
 * 
 */

void get_file_data(FILE* file, Event *event, Arg* arg, PrevDate* prev){

    char line[MAX_LINE_LEN];
    char* token;
    char repeat[20] = "";

    while (fgets(line, sizeof(line), file) != NULL) {              //parsing through the given file, line by line.
        
        char token[MAX_LINE_LEN];
        sscanf(line, "%[^:]", token);

        if (strcmp(token, "DTSTART") == 0) {                        //processes DTSTART: line
            sscanf(line, "DTSTART:%4s%2s%2sT%2s%2s", event->start_year, event->start_month,
                   event->start_day, event->start_hour, event->start_min);

        } else if (strcmp(token, "DTEND") == 0) {                   //processes DTEND: line
            sscanf(line, "DTEND:%4s%2s%2sT%2s%2s", event->end_year, event->end_month,
                   event->end_day, event->end_hour, event->end_min);

        } else if (strcmp(token, "LOCATION") == 0) {                //processes LOCATION: line
            sscanf(line, "LOCATION:%[^\n]", event->location);

        } else if (strcmp(token, "SUMMARY") == 0) {                 //processes SUMMARY: line
            sscanf(line, "SUMMARY:%[^\n]", event->summary);

        } else if (strcmp(token, "RRULE") == 0){                    //processes RRULE: line
            sscanf(line, "RRULE:FREQ=WEEKLY;WKST=WE;UNTIL=%[^T]", repeat);
    
        } else if (strncmp(line, "END:VEVENT", 10) == 0){           //checks if an event has ended. 
            int x = within_range(event, arg);
            if (x == 0) {
                if (strcmp(repeat, "") == 0){                       //prints event in required format.
                    print_output(event, prev);
                } else {
                    print_repeat(event, repeat, prev);              //prints repeated events.
                    strcpy(repeat, "");
                }
            }

        }

    }
    
}

/**
 * Function: print_repeat
 * ----------------------
 * @brief The print_repeat function prints the event information repeatedly, based on the given event's start day 
 *        and the specified "UNTIL" date.
 * @param event A pointer to the Event struct variable containing event information.
 * @param untill A pointer to the string representing the "UNTIL" date from a RRULE line.
 * @param prev A pointer to the PrevDate struct variable for handling recurring events.
 * 
 */

void print_repeat(Event* event, char* untill , PrevDate* prev){

    int untill_day;                                  //untill day in integer-format.
    sscanf(untill + 6, "%2d", &untill_day );    
    int file_day = atoi(event->start_day);           //start day in integer-format.
    

    while (file_day <= untill_day ){                 //loop untill start day is greater than the untill day.
        print_output(event, prev);
        file_day += 7;
        if (file_day > untill_day){
            return;
        }
        sprintf(event->start_day, "%02d", file_day);

    }
 
}

/**
 * Function: month_name
 * --------------------
 * @brief The month_name function returns the corresponding name of the month of the string being pointed to.
 * @return const char*: Returns a pointer to the corresponding month name as a string.
 *         If the provided month string is not valid, an empty string is returned.
 * 
 */

const char* month_name(char* month){

    if (strcmp(month, "01") == 0) {
        return "January";
    }
    else if (strcmp(month, "02") == 0) {
        return "February";
    }else if (strcmp(month, "03") == 0) {
        return "March";
    }
    else if (strcmp(month, "04") == 0) {
        return "April";
    }
    else if (strcmp(month, "05") == 0) {
        return "May";
    }
    else if (strcmp(month, "06") == 0) {
        return "June";
    }
    else if (strcmp(month, "07") == 0) {
        return "July";
    }
    else if (strcmp(month, "08") == 0) {
        return "August";
    }
    else if (strcmp(month, "09") == 0) {
        return "September";
    }
    else if (strcmp(month, "10") == 0) {
        return "October";
    }
    else if (strcmp(month, "11") == 0) {
        return "November";
    }
    else if (strcmp(month, "12") == 0) {
        return "December";
    }
    return "";
}

/**
 * Function: convertTo12HourFormat
 * -------------------------------
 * @brief The convertTo12HourFormat function converts a given time in 24-hour format to a 12-hour format with AM/PM indication.
 * @param hour24 A pointer to the string representing the hour in 24-hour format.
 * @param min A pointer to the string representing the start or end minute.
 * @param conv_hour A pointer to the character array for storing the converted time.
 * @return char*: Returns a pointer to the converted time in the format "HH:MM AM/PM".
 *         If the provided hour24 is not within the valid range (0-24), conv_hour is set to an empty string, and NULL is returned.
 * 
 * 
 */

char* convertTo12HourFormat(char* hour24, char* min, char* conv_hour) {

    int num = atoi(hour24);           // Convert 24-hour format string to integer.

    if (num < 0 || num > 24) {        //check if passed time value is within possible 24 hours.
        conv_hour[0] = '\0';
        return NULL;
    }

    int hour;
    const char* ampm;

    if (num % 12 == 0) {
        hour = 12;
    }
    else {
        hour = num % 12;
    }

    if (num < 12) {               //checks AM or PM.
        ampm = "AM";
    }
    else {
        ampm = "PM";
    }

    sprintf(conv_hour, "%*d:%s %s", 2, hour, min, ampm);
    return conv_hour;
}

/**
 * Function: print_output
 * ----------------------
 * @brief The print_output function prints the formatted output for a given event.
 *        It converts the start and end time to 12-hour format, retrieves the corresponding month name,
 *        and and updates the previous date information in the PrevDate struct variables.
 * @param event A pointer to the Event struct variable containing the event information.  
 * @param event A pointer to the Event struct variable containing event information.
 * @param prev A pointer to the PrevDate struct variable for handling recurring events.
 * 
 */

void print_output(Event* event, PrevDate* prev) {

    char count[MAX_LINE_LEN];

    char s_hour[10];
    char e_hour[10];
    convertTo12HourFormat(event->start_hour, event->start_min, s_hour);        //converts 24-hour event start time to to 12-hour format.
    convertTo12HourFormat(event->end_hour, event->end_min, e_hour);            //converts 24-hour event end time to to 12-hour format.

    const char* mon_name = month_name(event->start_month);                 //gets corresponding month name of event start month.
    if (strcmp(event->start_year, prev->prev_year) != 0 || strcmp(event->start_month, prev->prev_month) != 0 || strcmp(event->start_day, prev->prev_day) != 0) {         //checks if current event date matches previous event date.
        if (prev->prev_year[0] != '\0') {
            printf("\n");
        }
        printf("%s %s, %s\n", mon_name, event->start_day, event->start_year);
        sprintf(count, "%s %s, %s\n", mon_name, event->start_day, event->start_year);
        print_dash(count);
    }

    printf("%s to %s: %s {{%s}}\n",s_hour, e_hour, event->summary, event->location);

    strcpy(prev->prev_year, event->start_year);          //updates the previous date with current date.
    strcpy(prev->prev_month, event->start_month);
    strcpy(prev->prev_day, event->start_day);
}

/**
 * Function: print_dash
 * --------------------
 * @brief The print_dash function prints a line of dashes based on the length of the provided string.
 * @param  count A pointer to a string which is used to determine the number of dashes to print.
 * 
 */

void print_dash(const char* count) {

    int counter = strlen(count) - 1;
    char dash[MAX_LINE_LEN] = "";
    while (counter != 0) {
        strcat(dash, "-");
        counter--;
    }
    printf("%s\n", dash);
}




    






