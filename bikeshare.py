import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city=input('Please choose city from chicago, new york city and washington: ').lower()
    while city.lower() not in  (CITY_DATA.keys()):
          print('Please enter a valid city ')
          city=input('Please choose city from chicago, new york city and washington: ').lower() 
    
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january', 'february', 'march', 'april', 'may', 'june','all']
    month=input('Please choose month from january, february, march, april, may, june or all: ').lower()
    
    while month.lower() not in (months):
          print('Please enter a valid month ')
          month=input('Please choose month from january, february, march, april, may, june or all: ').lower()
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
    day=input('Please choose day from Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all: ').lower()
    
    while day.lower() not in days: 
          print('Please enter a valid day ')
          day=input('Please choose day from Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all: ')    
      
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
    
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month.lower() != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day.lower() != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day_of_week:', common_day_of_week)
    
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour:', common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('common Start Station:',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('common End Station:',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    most_trip = df['Start Station'] + ' to ' + df['End Station']
    print('most_frequent_combination:', most_trip.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('user types:', df['User Type'].value_counts())

    if city.lower() != 'washington':
        
    # TO DO: Display counts of gender
        print('gender:', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest Year:', df['Birth Year'].min())
        print('Most Recent Year:', df['Birth Year'].max())
        print('Most Common Year:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def Display_Raw_Data(df):
    runs = 0
    while True:
        raw_data = input('Would you like to view five rows of the data? Enter yes or no?').lower()

        if raw_data == 'yes':
            runs += 1
            print(df.iloc[(runs-1)*5:runs*5])
        elif raw_data == 'no':
            break    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        Display_Raw_Data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Good bye')
            break


if __name__ == "__main__":
    main()