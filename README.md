# bikeshare
The main program is 'bikeshare_main_with_functions.py'

It loads the csv file that's in this repository

The program seems to work fine until it uses the 'user_stats' function.  If I'm right about when in the program it fails, it's in 'user_stats' (line 423 in 'bikeshare_main_with_functions.py' that the KeyError is generated.  (See file 'keyerror-gender.py', the error says " KeyError: 'Gender' ")

Now, I do not use 'Gender' as a key in any of the dictionaries within the program.  So my guess as to why I'm getting a KeyError is that 'Gender' is a column heading in the csv file.  But 'Gender' is the column name, so I don't see why this would be an issue.

I wrote a test program ('test.py') with most of the code from the 'user_stats' function.  It loads and uses the csv file just fine.

So not sure where the key error is at this point.

A couple other notes: 'bikeshare_main_with_functions.py' is not set up to automatically read 'nyc_short.csv' ... and my program worked when I had the functions in separate file that the main program called.  For whatever reason, Udacity wanted everything in a single file, which is the 'bikeshare_main_with_functions.py' file included here.

Thanks for your help,

Aren Scanlan-Emigh
aren.se@gmail.com 
