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

    while True :
      city = input("\nWould you like to see data for chicago,new york city,or washington? \n").lower()
      if city in ('new york city', 'chicago', 'washington'):
        break
      else:
        print("Oops,you entered invalid city.")
        continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
      month = input("\nWould you like to see data for a particular month? if so,please enter january, february, march, april, may, june or type 'all' to apply no month filter? \n").lower()
      if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        break
      else:
        print("Oops,you entered invalid month.")
        continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
      day = input("\nWould you like to see data for a particular day? If so, please enter sunday, monday, tuesday, wednesday, thursday, friday, saturday or type 'all' to apply no day filter? \n").lower()
      if day in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        break
      else:
        print("Oops,you entered invalid day.")
        continue

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])



    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df





def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month :', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day of week :', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most common hour :', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most commomly used start station:' , most_common_start_station)

    # TO DO: display most commonly used end station

    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('Most commomly used end station:' , most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station_cobination = df[['Start Station', 'End Station']].mode().loc[0]
    print("Most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station_cobination[0], most_common_start_end_station_cobination[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time :' , total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time :' , mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nCounts of user types :\n' , user_types)

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")


    # TO DO: Display earliest, most recent, and most common year of birth
    # Display earliest year of birth
    try:
      earliest_year = df['Birth Year'].min()
      print('\nEarliest Year:', earliest_year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    # Display most recent year of birth
    try:
      most_recent_year = df['Birth Year'].max()
      print('\nMost Recent Year:', most_recent_year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    # Display most common year of birth

    try:
      most_common_year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', most_common_year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: get user input to see some raw data

    line_number = 1
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[line_number : line_number + 5])
            line_number = line_number + 5
        else:
            break



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
