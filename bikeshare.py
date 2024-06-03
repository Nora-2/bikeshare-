import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cityNAME=''
    while cityNAME.lower() not in CITY_DATA:
        cityNAME =  input('\nWhich city do you want to explore (Chicago, New York , Washington) \n> ').lower()
        if cityNAME.lower() in CITY_DATA:
          
            city = CITY_DATA[cityNAME.lower()]
        else:
          
            print("Sorry we can't reach the name of the city to analyze data, Please input either chicago, new york city or washington.\n")


    # TO DO: get user input for month (all, january, february, ... , june)
    monthNAME = ''
    while monthNAME.lower() not in MONTH_DATA:
        monthNAME = input("\nPlease enter the name of the month to filter data? or just say 'all' to apply no month filter.\n(e.g. all, january, february,march, april, may, june,...)\n")
        if monthNAME.lower() in MONTH_DATA:
            month = monthNAME.lower()
        else:
            
            print("\nSorrywe can't reach the  name of the month to filter data,\n Please input either 'all' to apply no month filter or january, february, ... , june.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dayNAME = ''
    while dayNAME.lower() not in DAY_DATA:
        dayNAME = input("\nPlease enter the name of the day to filter data?or just say 'all' to apply no day filter (E.g. monday, tuesday, ... sunday)\n")
        if dayNAME.lower() in DAY_DATA:
            #We were able to get the name of the month to analyze data.
            day = dayNAME.lower()
        else:
            #We were not able to get the name of the month to analyze data so we continue the loop.
            print("Sorry we were not able to get the name of the day to filter data, Please input either 'all' to apply no day filter or monday, tuesday, ... sunday.\n")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH_DATA.index(month)

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    commonMonth = df['month'].mode()[0]
    print(f"The most common month from the given fitered data is:-{MONTH_DATA[commonMonth].title()}")

    # TO DO: display the most common day of week
    commonDayOfWeek = df['day_of_week'].mode()[0]
    print(f"The most common day of week from the given fitered data is:- {commonDayOfWeek}")

    # TO DO: display the most common start hour
    commonStartHour = df['hour'].mode()[0]
    print(f"The most common start hour from the given fitered data is:- {commonStartHour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    StartStation=df['Start Station'].mode()[0]
    print(f'\nMost commonly used start station is:-{StartStation} ')
    
    # TO DO: display most commonly used end station
    endStation=df['End Station'].mode()[0]
    print(f'\nMost commonly end station is:- {endStation} ')
    # TO DO: display most frequent combination of start station and end station trip
#     df['Start & End'] = df['Start Station'].str.cat(df['End Station'], sep='==>> ')
    mostFrequantCombination=df[['Start Station', 'End Station']].mode()[0]
    print(f'\nMost frequent combination of start station and end station trip is:- {mostFrequantCombination} ')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTravel = df['Trip Duration'].sum()
    print(f"Total travel time :- { totalTravel}")

    # TO DO: display mean travel time

    meanTravel = df['Trip Duration'].mean()
    print("Mean Travel time :", meanTravel)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCounts of user types: \n',df['User Type'].value_counts())
   
        # TO DO: Display counts of gender
    try:
        print('\nCounts of gender: \n',df['Gender'].value_counts())
    except:
        print('\nSorry, their is no "Gender" informations like this ')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:

        earliestBirth = df['Birth Year'].min()
        mostRecentBirth = df['Birth Year'].max()
        mostCommonBirth = df['Birth Year'].mode()[0]
        print(f'Earliest birth from the given fitered data is:- {earliestBirth}\n')
        print(f'Most recent birth from the given fitered data is: {mostRecentBirth}\n')
        print(f'Most common birth from the given fitered data is: {mostCommonBirth}\n' )
       
    except:
        print('\nSorry, Whasington has no "year of birth" informations')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
