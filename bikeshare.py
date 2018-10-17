## bikeshare_main.py
## Aren Scanlan-Emigh, aren.se@gmail.com
## Developed as part of the Udacity Data Analyst Nanodegree program, Term 1
## July, 2018

## This was built with Pandas 0.23


import pandas as pd
import numpy as np
import time
import datetime
import calendar as cal
import math
import statistics as stats

####################### Citations ############################################
#Source for code for comma separators in large numbers ("{:,}".format(number)):
#https://www.geeksforgeeks.org/print-number-commas-1000-separators-python/

# See also citations embedded with the code below.
##############################################################################


##############################################################################
####################### PRELIMINARY SETUP OF LISTS / VARIABLES ###############

###### VARIABLES FOR CHOOSING CITY ######
# For choosing the right csv file
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'
              }

# This variable stores the user's choice
city_choice = ''    

# 'cities_lookup' is used to return the full city name regardless of 
# alternative inputs like 'chic', 'dc', or 'NYC'.
cities_lookup = {'chicago': 'chicago', 
                 'chic' : 'chicago',
                 'c' : 'chicago',
                 'new york city' : 'new york city', 
                 'new york' : 'new york city', 
                 'nyc' : 'new york city', 
                 'n' : 'new york city',
                 'washington' : 'washington', 
                 'w' : 'washington',
                 'dc' : 'washington', 
                 'd.c.' : 'washington'
                 }
# Make a list of keys from the above dictionary, for purposes of detecting 
# invalid input later.
city_list = cities_lookup.keys()
# note: this produces a list with repeated, and therefore redundant, values
# originally I had city_list = list(set(cities_lookup.keys())), but it
# returned << TypeError: 'list' object is not callable >> and the Udacity
# mentor and I couldn't figure it out.  So my solution works, but is a little
# inefficient.

###### END OF VARIABLES FOR CHOOSING CITY ######


###### VARIABLES FOR CHOOSING MONTH TO FILTER BY ######
# This variable stores the user's choice
month_choice = ''
#### MAY NEED TO CHANGE TO THE MONTH INDEXES OF 1 - 12
# 'month_lookup' is used to return the full month name regardless of 
# alternative inputs like 'jan'.
month_lookup = {'january': 'january', 
                 'jan' : 'january',
                 'february': 'february', 
                 'febuary' : 'february',
                 'feb' : 'february',
                 'march': 'march', 
                 'mar' : 'march',
                 'april': 'april', 
                 'apr' : 'april',
                 'may': 'may', 
                 'jun' : 'june',
                 'june': 'june',
                 'all' : 'all',
                 'a' : 'all'
                 }

# also for detecting invalid input
month_list = month_lookup.keys()


# month_numbers - see notes in load_data function
month_numbers = {'january' : 1, 
                 'february' : 2, 
                 'march' : 3, 
                 'april' : 4, 
                 'may' : 5, 
                 'june' : 6,
                 }

###### END OF VARIABLES FOR CHOOSING MONTH ######



###### VARIABLES FOR CHOOSING DAY TO FILTER BY ######
# This variable stores the user's choice
day_choice = ''
#### MAY NEED TO CHANGE TO THE DAY INDEXES OF 0-6
# 'day_lookup' is used to return the full day name regardless of 
# alternative inputs like 'Tues'.
day_lookup = {'monday': 'monday', 
                 'mon' : 'monday',
                 'tuesday': 'tuesday', 
                 'tues' : 'tuesday',
                 'tu': 'tuesday', 
                 'wednesday' : 'wednesday',
                 'wed': 'wednesday', 
                 'thursday' : 'thursday',
                 'thurs': 'thursday', 
                 'th' : 'thursday',
                 'friday': 'friday',                   
                 'fri': 'friday',
                 'saturday': 'saturday',                   
                 'sat': 'saturday',
                 'sunday': 'sunday',                   
                 'sun': 'sunday',
                 'all' : 'all',
                 'a' : 'all'
                 }

# Make a list of keys from the above dictionary, for purposes of detecting invalid input later.
day_list = day_lookup.keys()


# day_numbers - see notes in load_data function
day_numbers = {'monday': 0, 
                 'tuesday': 1, 
                 'wednesday': 2, 
                 'thursday': 3, 
                 'friday': 4, 
                 'saturday': 5, 
                 'sunday': 6
                 }

###### END OF VARIABLES FOR CHOOSING DAY ######

##############################################################################
################### END OF PRELIMINARY SETUP OF LISTS / VARIABLES #########
##############################################################################



###########################################################################
##################Define functions to be called later#######################
##############################################################################

def filter_city():
    """
    Asks user to specify a city to analyze, as well as a day, month, or both
    or neither

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    ## get user input for city (chicago, new york city, washington).
    # Make a 1st attempt to get the city choice from the user:
    print('*** Would you like to investigate data for Chicago, New York, '
          'or Washington?')
    print('')
    city_choice = input().lower()

    # If user's city choice is invalid, try again:
    while True:
        if city_choice not in city_list:
            print('Invalid entry. (You typed {}.)\n'.format(city_choice))
            print('Please enter \'chicago\', \'new york\', or \'washington\' (or \'c\', \'n\', \'w\'): ')
            city_choice = input().lower()
        else:
            break
        
    # The next line just avoids having to reference the city as
    # 'cities_lookup[city_choice]' later in the program.        
    city_choice = cities_lookup[city_choice] 

    return city_choice


###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   
def filter_month():
    """
    Asks user to decide specify which month (if any) to filter the data by

    Returns:
        (str) month_choice - the month by which data will be filtered
    """
    # get user input for month (all, january, february, ... , june)
    # Make a 1st attempt to get the user's choice:
    print('*** Pick a month to examine, or type \"all\".')
    month_choice = input().lower()
    
    
    # If user's choice is invalid, try again:
    while True:
        if month_choice not in month_list:
            print('*** Invalid entry. (You typed {}.) \n'.format(month_choice))
            print('Please enter one of these choices:',
                  '\nJanuary (jan), \nFebruary (feb), \nMarch (mar),'
                  '\nApril (apr), \nMay, \nJune (jun), \nall,'
                  '\nEnter your choice:')
            month_choice = input().lower()
        else:
            if month_choice == 'all':
                print('\nYou chose to look at ride data for all months.')
            else:
                print('You chose {}.'.format(month_lookup[month_choice].title()))
            break

    month_choice = month_lookup[month_choice]

    return month_choice


###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###  
def filter_day():
    """
    Asks user to decide specify which day of the week (if any) to filter the
    data by

    Returns:
        (str) day_choice - the day by which data will be filtered
    """
    # get user input for day (all, Monday, Tuesday ... Sunday)
    # Make a 1st attempt to get the user's choice:
    print('\n*** Pick a day of the week to examine, or type \"all\".')
    day_choice = input().lower()
    
    
    # If user's choice is invalid, try again:
    while True:
        if day_choice not in day_list:
            print('Invalid entry. (You typed {}.) \n'.format(day_choice))
            print('Please enter one of these choices:',
                  '\nMonday (mon), \nTuesday (tues), \nWednesday (wed),'
                  '\nThursday (thurs), \nFriday (fri), \nSaturday (sat),'
                  '\nSunday (sun), \nall,'
                  '\nEnter your choice:')
            day_choice = input().lower()
        else:
            if day_choice == 'all':
                print('\nYou chose to look at ride data for all days of the',
                      'week.\n')
            else:
                print('\nYou chose {}.\n'.format(day_lookup[day_choice].title()))
            break

    day_choice = day_lookup[day_choice]

    return day_choice




def load_data(city_choice, month_choice, day_choice):
    """
    Loads data for the specified city and filters by month and day,
    if applicable.
    Adds columns containing only the starting day and month for each bike trip.

    Args:
        (str) city_choice - name of the city to analyze
        (str) month_choice - name of the month to filter by, or "all" to apply no month filter
        (str) day_choice - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data for chosen city ('city_choice' as key in 'cities_lookup' 
    # --> a city name (as value)
    # --> city name (as key) in 'CITY_DATA' --> csv file (as value)
    # --> csv file as argument for 'read_csv'
    df = pd.read_csv(CITY_DATA[cities_lookup[city_choice]])


    # convert csv data to 'datetime' format
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    
    # add columns containing only the month, day, and starting hour for each
    # bike trip
    df['Start Month'] = df['Start Time'].dt.month # returns 1-12 (jan-dec)
    df['Start Day'] = df['Start Time'].dt.weekday # returns 0-6 (mon-sun)
    df['Start Hour'] = df['Start Time'].dt.hour

    # convert month_choice, day_choice from names ('June', 'Tuesday') back 
    # to numbers (6, 1).  This is inelegant, but at time of writing I need to 
    # be smart about not spending time rewriting the entire program.



    # filter by day and/or time. If user selected 'all', filter isn't applied
    if (month_choice == 'all') and (day_choice == 'all'):
        pass
    elif month_choice == 'all':
        day_number = day_numbers[day_choice]
        df = df[df['Start Day'] == day_number]
    elif day_choice == 'all':
        month_number = month_numbers[month_choice]
        df = df[df['Start Month'] == month_number]
    else:
        month_number = month_numbers[month_choice]
        day_number = day_numbers[day_choice]
        df = df[df['Start Day'] == day_number]
        df = df[df['Start Month'] == month_number]

    return df


def time_stats(df):
    """Returns statistics on the most frequent times of travel."""

    print('\n*** Most Frequent Times of Travel:')
    start_time = time.time()

    # display the most common month
    month_mode = df['Start Month'].mode()[0]
    month_mode = cal.month_name[month_mode]
    print('   * The month with the most trips was {}.'.format(month_mode))


    # display the most common day of week
    day_mode = df['Start Day'].mode()[0]
    day_mode = cal.day_name[day_mode]
    print('   * {} was the most common day for bike trips.'.format(day_mode))


    # display the most common start hour
    hour_mode = df['Start Hour'].mode()[0]
    ## do same for hour_mode as for day_mode
    print('   * The hour in which the most trips started was {}:00.'.format(hour_mode))


    elapsed_time = str(round((time.time() - start_time), 3))
    print("\n[This took {} seconds.]".format(elapsed_time))
    print('-'*40, '\n')
    return month_mode, day_mode, hour_mode


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('*** Most Popular Stations and Trip:')
    start_time = time.time()

    # display most commonly used start station
    start_station_mode = df['Start Station'].mode()[0]
    print('* {} was the most common starting station.'.format(start_station_mode))

    # display most commonly used end station
    end_station_mode = df['End Station'].mode()[0]
    print('* {} was the most common ending station.'.format(end_station_mode))


    # display most frequent combination of start station and end station trip
    trip_pair_list = []
    temp_pair = ('','')
    temp_end = ''
    temp_start = ''
    size = df.shape[0]


    for i in range(size):
        temp_start = df['Start Station'][i]
        temp_end = df['End Station'][i]
        temp_pair = (temp_start, temp_end)
        trip_pair_list.append(temp_pair)
    
    mode_trip_pair = stats.mode(trip_pair_list)
    # (citation for use of stats.mode: 
    # https://www.geeksforgeeks.org/python-statistics-mode-function/   )
    
    
    print ('* The most common combination of stations is \n  {}.'.format(mode_trip_pair))
    
    count_trip_mode = trip_pair_list.count(mode_trip_pair)
    print ('* It occurred {} times.'.format(count_trip_mode))


    elapsed_time = str(round((time.time() - start_time), 6))
    print("\n[This took {} seconds.]".format(elapsed_time))
    print('-'*40, '\n')
#    return start_station_mode, end_station_mode, mode_trip_pair, count_trip_mode



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('*** Trip Duration:')
    start_time = time.time()


    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    time_in_days = total_travel_time // (24 * 60)
    time_in_years = total_travel_time // (24 * 60 * 365.2425)
    print('* The total travel time for all trips in the selected data was')
    print('   *    {:,} minutes'.format(total_travel_time))
    print('   * or {:,} days'.format(time_in_days))
    print('   * or {:,} years'.format(time_in_years))


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mtt_hour = int(mean_travel_time // 60)
    mtt_min = int(mean_travel_time % 60)
    print('\n* The mean travel time per trip for all trips in the selected data',
          'was {} hours {} minutes.'.format(mtt_hour, mtt_min))


    elapsed_time = str(round((time.time() - start_time), 3))
    print("\n[This took {} seconds.]".format(elapsed_time))
    print('-'*40, '\n')



def user_stats(df):
    """Returns statistics on bikeshare users."""

    print('\n*** Bikeshare User Stats:')
    start_time = time.time()


    # Display counts of user types
    trip_count = df['User Type'].count()
    subscriber_count = df[df['User Type'] == 'Subscriber'].count()[0]
    s_pct = int(subscriber_count / trip_count * 100)
    customer_count = df[df['User Type'] == 'Customer'].count()[0]
    c_pct = int(customer_count / trip_count * 100)
    
    print('* Of {:,} trips:'.format(trip_count))
    print('   * {:,} ({}%) were purchased by subscribers, and'.format(subscriber_count, s_pct))
    print('   * {:,} ({}%) were purchased by non-subscribing customers.'.format(customer_count, c_pct))


    # Display counts of gender
    gender_count = df['Gender'].count()
    female_count = df[df['Gender'] == 'Female'].count()[0]
    f_pct = int(female_count / gender_count * 100)
    male_count = df[df['Gender'] == 'Male'].count()[0]
    m_pct = int(male_count / gender_count * 100)
    
    print('\n* In {:,} trips, users identified their gender {:,} times, as:'.format(trip_count, gender_count))
    print('   * {:,} female ({}%)'.format(female_count, f_pct))
    print('   * {:,} male ({}%))'.format(male_count, m_pct))


    # Display earliest, most recent, and most common year of birth
    year_count = df['Birth Year'].count()
    yr_pct = int(year_count / trip_count * 100)
    earliest_year = df['Birth Year'].min()
    most_recent_year = df['Birth Year'].max()
    year_mode = df['Birth Year'].mode()[0]

    print('''\n* In {:,} of {:,} trips ({}%) the user recorded their year of birth.
    '''.format(year_count, trip_count, yr_pct))
    print('   * The oldest user was born in {}.'.format(earliest_year))
    print('   * The youngest user was born in {}.'.format(most_recent_year))
    print('   * The most common birth year was {}.'.format(year_mode))


    elapsed_time = str(round((time.time() - start_time), 6))
    print("\n[This took {} seconds.]".format(elapsed_time))
    print('-'*40, '\n')

######## END OF FUNCTIONS #################################################
###########################################################################

###########################################################################
######## MAIN PROGRAM #####################################################
print('Bikeshare Data\nAren Scanlan-Emigh\n2018')
name = input('*** Please enter your name: \n\n')
print('* Welcome, {}.'.format(name))
print('* Let\'s investigate some US bikeshare data.')
print('* You can now choose a city, month, and day to analyze.')
print('\n** try common abbreviations (nyc, dc, jan) \n** or single letters (n = New York, w = Washington, a = all)')
print('\n\n')

# Get user's choices for filtering the bikeshare data 
city_n = filter_city()
month_n = filter_month()
day_n = filter_day()

# summarize choices:
print('-'*40)
print('\nSummary: you chose data for\n')
print('  > city: ', city_n.title())

if month_n == 'all':
    print('  > month: {}'.format(month_n.title()))
else:
    print('  > month: {}'.format(month_n.title()))

if city_n == 'all':
    print('  > day: {}'.format(day_n.title()))
else:
    print('  > day: {}'.format(day_n.title()))

print('-'*40)


# load and filter data according to user's choices:
df = load_data(city_n, month_n, day_n)


###########################################################################
# return stats for selected time period
time_stats(df) # info about starting times of trips
station_stats(df) # info about stations at which bikes were rented
trip_duration_stats(df) # total and mean travel time
user_stats(df) # info about bikeshare users