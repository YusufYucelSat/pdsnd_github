"""
This Python code explores data related to bike share systems for three major cities in the United States: Chicago, New York City, and Washington. 
It imports the data and answers interesting questions about it by computing descriptive statistics. 

"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
            'new york city': 'new_york_city.csv',
            'washington': 'washington.csv' }


months=['january', 'february', 'march', 'april', 'may','june','all']
weekdays=['monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bike share data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
    while city not in CITY_DATA.keys():
        city = input("Invalid input. Please enter Chicago, New York City, or Washington: ").lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month would you like to filter by? (all, january, february, ..., june): ").lower()
    while month not in months:
        month = input("Invalid input. Please enter a valid month or 'all': ").lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day of the week would you like to filter by? (all, monday, tuesday, ..., sunday): ").lower()
    while day not in weekdays:
        day = input("Invalid input. Please enter a valid day or 'all': ").lower()
    
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
    
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday
    df['hour']=df['Start Time'].dt.hour
    
# filter by month
    if month != 'all':
        month=months.index(month)+1
        df=df[df['month']==month]
        
    if day != 'all':
        day=weekdays.index(day)
        df = df[df['day_of_week'] == day]
        
# df['month']= (months[month-1])
# df['day_of_week']=weekdays[day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', months[popular_month-1])
    
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:', weekdays[popular_day])
    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most popular Start Station is ', df['Start Station'].mode()[0])
    
    # display most commonly used end station
    print('The most popular End Station is ', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print('\nMost Frequent Combination of Start and End Station Trips: \n\n', df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total Trip Duration is ', df['Trip Duration'].sum )

    # display mean travel time
    print('Mean Trip Duration is ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bike share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types=df['User Type'].value_counts()
    print('The user types count:', user_types)

    # Display counts of gender
    try:
        gender=df['Gender'].value_counts()
        print('The gender counts:',gender)
    except:
        print('We are sorry ! There is no available gender data')

    # Display earliest, most recent, and most common year of birth
    try:
        print('Earliest year of Birth is ', df['Birth Year'].min())
        print('Most recent year of Birth is ', df['Birth Year'].max())
        print('Most common year of Birth is ', df['Birth Year'].mode()[0])
    except:
        print('We are sorry ! There is no available birth year data')
        
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
        
        
        #To prompt the user whether they would like want to see the raw data
        enter = ['yes','no']
        user_input = input('Would you like to see more data? (Enter:Yes/No).\n')
        
        while user_input.lower() not in enter:
            user_input = input('Please Enter Yes or No:\n')
            user_input = user_input.lower()
        n = 0        
        while True :
            if user_input.lower() == 'yes':
        
                print(df.iloc[n : n + 5])
                n += 5
                user_input = input('\nWould you like to see more data? (Type:Yes/No).\n')
                while user_input.lower() not in enter:
                    user_input = input('Please Enter Yes or No:\n')
                    user_input = user_input.lower()
            else:
                break           

                
                
        restart = input('\nWould you like to restart? (Enter:Yes/No).\n')
        #check wheather the user is entering the valid entry or not
        while restart.lower() not in enter:
            restart = input('Please Enter Yes or No:\n')
            restart = restart.lower()
        if restart.lower() == 'no':
            print('Thank you. See you again!!!')
            break    
        

if __name__ == "__main__":
	main()        

