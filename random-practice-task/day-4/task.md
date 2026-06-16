A manager says:

I have 3 log files.

I want to know which application is the most problematic.



Requirements

Write a script that:

Reads all 3 files.
Counts ERRORs in each file.
Prints:
app1.log -> 2 errors
app2.log -> 3 errors
app3.log -> 0 errors
Determine the worst application.

Output:

MOST PROBLEMATIC APPLICATION

app2.log

TOTAL ERRORS: 3
New Requirement

Create a function:

def count_errors(filename):

This function should:

Accept a filename
Open the file
Count errors
Return the count

Example:

count = count_errors("app1.log")