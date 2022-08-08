# Call Time Logger
I wrote this to log the times I get calls.

Once the times are logged you can compute when it is likely to be the busiest

## Installation

This project does not currently require running any install scripts and the only requirement is python3
simply run it by clicking on it, or "py call.py" or "python3 call.py" ("python call.py" might work on newer Linux distros)

## How to use call.py

The first thing you will see should be the following:

"Log-file: "0callHistory.txt" was created in the following dir: "./call_logs/""

this file will log all of your commands, most command responses,and general inputs into from call.py. I Use it for notes, so I can go back and review at a later date.

Next, you will be given the following prompt:

"Hit "ENTER" for DEFAULT File Name:"

If you hit ENTER it will automatically generate the file with the current date.

However, you can enter a custom filename, but "01File_Reader_Final.py" expects the format listed below. You may need to use this if you need to restart the program, but the day has changed, and need to reload the "previous days" file.

**calls_ddmmyyyy**

(ddmmyyyy example: 01012023)

You do not need to include a file extension, but if you include the ".txt" it will not add it again. 

It will then automatically create the file, but you can also manually write the to the file by typing "write".

The created files will write to the call_logs file.


To log the call time simply type: "y" and hit the enter, or the return key. You must do this manually each time. Each log will rewrite to the file.

to can end a call with the "ecc" or "epc" command

To properly exit, type "exit", and press enter or the return key. If you did not type "write", and didn't log any times, it will not create a file.

You will be given the following prompt if a file already exists:

calls_xxxxxxxx.txt Detected already. Please choose next action

File size indicates *** DATA IS PRESENT! ***
Size: __ BYTES

CHOOSE AN OPTION:
1. Open
2. Overwrite
input decision: 

1. If you choose open. it will open and attempt to continue off from where it left off.
2. Overwrite. It will overwrite the file.

## How to use 01File_Reader_Final.py
This is in the call_logs file.

the file is named that way to keep them together, and in the proper order they should be run.
Note: this is only true for 01 and 02. The others can be run freely (as long as 01, and 02 have been run at least once with data).

To run: type "start", and hit enter, or return. you can run "print" to see the data that it processed.
Notes: This is meant to be run after a session, and while you are on the "current one", and have logged a new file with "write"
Example: you already have "calls_01012023.txt” and have just saved "calls_01022023.txt". It will skip the 01022023 file, and only run on the 01012023. This is because it is assumed that you are working on the most recent file.


## How to use the 02callTotaler

To run simply click on it, or run it with "py 02callTotaler.py" or "python3 02callTotaler.py"
 
this will tally the calls and write to 2 log files for use in the other 3 programs.


## How to use 03callTimes

To run click on it or run "py 03callTimes.py" or "python3 03callTimes.py"

This should work if you have data and ran it successfully through the above 01File_Reader_Final.py, and 02callTotaler.py

This should show the days of the week, and the call counts for those days. it will also show a breakdown of the times of the calls separated by hours.

Note: this is currently tuned for a night shift.

I might update it to be customizable, or "dynamic" in the future.


## How to use 04callStats

To run click on it or run "py 04callStats.py" or "python3 04callStats.py"

This computes statistics from the data.


## How to use 05adjustedCallTimes

To run click on it, run "py 05adjustedCallTimes.py", or run "python3 05adjustedCallTimes.py"

This is like 03callTimes but is tuned for the shift (this wouldn't be useful if it were a day shift).

This is because on 12-hour nights the shift is split between 2 days and calls on a Monday shift can come in on Tuesday on top of having a Tuesday shift. This also includes a breakdown of the number of calls per month.


