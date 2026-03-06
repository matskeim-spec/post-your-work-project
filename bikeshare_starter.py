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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print(f'Most common month: {most_common_month}')

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print(f'Most common day of week: {most_common_day}')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print(f'Most common start hour: {most_common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f'Most commonly used start station: {most_common_start_station}')

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f'Most commonly used end station: {most_common_end_station}')

    # display most frequent combination of start station and end station trip
    most_frequent_combination = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print(f'Most frequent combination of start station and end station: {most_frequent_combination}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'Total travel time: {total_travel_time}')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'Mean travel time: {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f'Counts of user types:\n{user_types}')

    # Display counts of gender
    gender_counts = df['Gender'].value_counts()
    print(f'Counts of gender:\n{gender_counts}')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print(f'Earliest year of birth: {earliest_year}')
        print(f'Most recent year of birth: {recent_year}')
        print(f'Most common year of birth: {common_year}')

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
