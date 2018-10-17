# bikeshare
I'm getting a KeyError:

KeyError: 0


linked to line 370 in "bikeshare.py", which is the second line here:

    for i in range(size):
        temp_start = df['Start Station'][i]
        temp_end = df['End Station'][i]
        temp_pair = (temp_start, temp_end)
        trip_pair_list.append(temp_pair)

Odd thing is that I don't get the error in a test file that uses the above code ("untitled11.py")

Thanks for your help,

Aren Scanlan-Emigh
aren.se@gmail.com 
