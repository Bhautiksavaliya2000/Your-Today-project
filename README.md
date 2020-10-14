# Your-Today-project
Python script will notify the user about the next lecture and open the meeting link in the default browser.

This app works using Four inputs.
1. Number of lectures in a day.
   -> Number should be an integer.

2. Starting time of all the lectures. (Ending time is not taken so it is better if continuous lectures)
   -> Time must be in HH:MM format. 
   -> Consider the 24 hours or 12 hours format and enter time accordingly.
   -> e.g. Enter 09:45 instead of 9:45.
   
3. Messages to show in notification when each lecture starts.
   -> Enter 'NA' if no lecture during a particular time.
   
4. Meeting links of all lectures.
   -> Enter 'NA' if a particular lecture has no link to attach.
   
If require to modify the timetable, then change the values in 'timetable.csv' that the program created in the current working directory.

