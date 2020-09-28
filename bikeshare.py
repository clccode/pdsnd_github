import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': '/Users/campbellcl/OneDrive/python/bikeshare-2/chicago.csv',
              'new york city': '/Users/campbellcl/OneDrive/python/bikeshare-2/new_york_city.csv',
              'washington': '/Users/campbellcl/OneDrive/python/bikeshare-2/washington.csv' }
            #above files show location on my local drive.
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
    while True:
        city = input('Please select Chicago, New York City, or Washington (upper or lower case): ').lower()

        if city in (CITY_DATA.keys()):
            print('It looks like you have chosen', city.title())
            break
        else:
            print("Sorry, that's not a valid city name. Please try again.")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Month: please select January, February, March, April, May, June, or all (upper or lower case): ").lower()
        if month in ["january", "february", "march", "april", "may", "june", "all"]:
            print(f"You chose {month.title()}.")
            break
        else:
            print("Sorry, that's not a valid selection. Please try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Day: please select Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all (upper or lower case): ").lower()
        if day in ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            print(f"You chose {day.title()}.")
            break
        else:
            print("Sorry, that's not a valid selection. Please try again.")

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
    if city == 'chicago':
        df = pd.read_csv('chicago.csv')
    elif city == 'new york city':
        df = pd.read_csv('new_york_city.csv')
    else:
        df = pd.read_csv('washington.csv')

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print(f'The most popular month (as a number of 1-6 for Jan-Jun) is {popular_month}.')

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    popular_day = df['day'].mode()[0]
    print(f'The most popular day of the week is {popular_day}.')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'The most popular start hour (listed from 0, or midnight, to 23, or 11pm) is {popular_hour}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'{popular_start_station} is the most commonly used start station.')

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'{popular_end_station} is the most commonly used end station.')

    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = round(df['Trip Duration'].sum()/60, 2)
    print(f'The total travel time for all bike rentals was {total_travel_time} minutes.')


    # TO DO: display mean travel time
    avg_travel_time = round(df['Trip Duration'].mean()/60, 2)
    print(f'The mean travel time for all bike rentals was {avg_travel_time} minutes.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts().to_frame())
    print()

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts().to_frame())
        print()
    else:
        pass

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        max_year = df['Birth Year'].min()
        print(f'The oldest customer was born in {int(max_year)}.')

        min_year = df['Birth Year'].max()
        print(f'The youngest customer was born in {int(min_year)}.')

        most_year = df['Birth Year'].mode()
        print(f'Most of the customers were born in {int(most_year)}.')

    else:
        pass


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

        # Asks the user if he/she would like to see raw data 5 rows at a time.
        i = 0
        raw_data = input("\nWould you like to see the raw data 5 rows at a time? Please answer yes or no: \n").lower()

        while True:
            if raw_data == 'no':
                break
            print(df[i:i+5])
            raw_data = input("\nWould you like to continue viewing raw data? Please answer yes or no: \n").lower()
            i += i+5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
