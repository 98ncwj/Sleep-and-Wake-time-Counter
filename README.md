Simple function to count total waking hours and sleeping hours in a schedule

function accepts a txt file containing schedules and writes output of total waking and sleeping hours in minutes

first line of text file input is number of cases followed by number of waking hours and respective waking hours 

example .txt:

2               

3		
05:00 06:00     
20:00 08:30     
01:00 01:30

2
06:00 09:00    
10:00 11:00  

//two cases in total 

//3 schedules
//sleep from 05:00 to 06:00, 20:00 to 08:30,..
//wake from 06:00 to 20:00, 08:30 to 01:00

//2 schedules
//sleep from 06:00 to 09:00, 10:00 to 11:00
//wake from 09:00 to 10:00

Output:

Case XX : WAKE SLEEP

output for example:

Case 1: 1830 840

Case 2: 60 240