# Call Time Logger
I wrote this to log the times I get calls.

Once the times are logged you can compute when it is likely to be the busiest

## Installation

This project does not require running any install scripts and the only requirement is python3
simply run it by clicking on it, or "py call.py" or "python3 call.py"

## How to use call.py

Once you click on it it you will be prompted for a filename.

it (01File_Reader_Final.py), expects the following format

**calls_ddmmyyyy**

(ddmmyyyy example: 01012023) 
You do not need to include a file extension (it will make a file called calls_ddmmyyyy.txt). 
you can have it create the file immediately by typing "write" (after you input the "calls_ddmmyyyy"

There are other included python projects need the above format.

The created files will write to the call_logs file.

You will likely see a reference to a "log file" this is for an unused feature that was going to log each line to a separate file for review like this "history" command in Powershell and linux shell (when on a call I would sometimes use my program for note taking, and it would have been helpful to save that info). I never implemented it, and I will likely remove it, and the reference to it here.

To log the call time simply type: "y" and hit the enter, or the return key. You must do this manually each time. Each log will rewrite to the file.

To properly exit, type "exit", and press enter or the return key. If you did not type "write", and didn't log any times, it will not create a file.


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

It will not run without processed data.

This computes statistics from the data.


## How to use 05adjustedCallTimes

To run click on it, run "py 05adjustedCallTimes.py", or run "python3 05adjustedCallTimes.py"

This is like 03callTimes but is tuned for the shift (this wouldn't be useful if it were a day shift).

This is because on 12-hour nights the shift is split between 2 days and calls on a Monday shift can come in on Tuesday on top of having a Tuesday shift. This also includes a breakdown of the number of calls per month.


