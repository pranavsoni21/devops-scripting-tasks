Real-World Scenario

It's 2:00 AM.

Your application is having issues.

Your manager says:

I don't want to manually search logs.

Create a script that tells me:

How many ERROR messages occurred
How many WARNING messages occurred
Show the actual ERROR lines
Your Challenge

Create a file:

app.log

with this content:

INFO Application started
INFO User login successful
ERROR Database connection failed
WARNING Memory usage high
INFO Request completed
ERROR Redis connection timeout
INFO Health check passed
WARNING Disk usage 85%
ERROR Payment service unavailable
Expected Output
========== LOG REPORT ==========

ERROR COUNT: 3

WARNING COUNT: 2

ERROR DETAILS:

ERROR Database connection failed

ERROR Redis connection timeout

ERROR Payment service unavailable
Rules

Use only:

open()
for loop
if statement
list