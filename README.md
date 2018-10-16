# bikeshare
The main program is 'bikeshare_main_with_functions.py'

It loads the csv file that's in this repository

The program seems to work fine until it uses the 'user_stats' function.  If I'm right about when it fails, it's at this point (line 423 in 'bikeshare_main_with_functions.py' that the KeyError is generated.  (See file 'keyerror-gender.py', the error says " KeyError: 'Gender' ")

Now, I do not use 'Gender' as a key in any of the dictionaries within the program.  So my guess as to why I'm getting a KeyError is that 'Gender' is a column heading in the csv file.

So I wrote a test program ('test.py') with most of the code from the 'user_stats' function.  It loads and uses the csv file just fine.

So not sure where the key error is at this point.

Thanks for your help.

Aren Scanlan-Emigh
aren.se@gmail.com 
