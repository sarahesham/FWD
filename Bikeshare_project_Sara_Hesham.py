# import the required libraries
import time
import pandas as pd
import numpy as np


# Required dictionaries
# Dictionary of the city names and their csv files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Dictionary of the covered months in the data
months = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'june':6, 'all': 'all'}

# Dictionary of days and the corresponding number
days = {0: 'Mon', 1: 'Tue', 2: 'WED', 3: 'THU', 4: 'FRI', 5: 'SAT', 6: 'SUN'}


# Required functions
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello!', 'Let\'s explore some US bikeshare data!', sep = '\n')
    print('='*70, '\n\n')
    print('1) Please type the required data as it is written in the following questions.')
#     print('='*70, '\n\n')
    print('2) If you wanna exit at any step in the program, just type "exit"')
    print('='*70, '\n\n')
    print("'let's start", '\n\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    flag = 0
    while(True):
        city = input('Which country you wanna explore?!\n (chicago, new york city, or washington)?!')
        city = city.lower().strip()
        if city == 'exit': 
            flag = 1 
            break
        if city not in CITY_DATA.keys():
            print('\nCity name error !!')
            print('please enter the city name as written in the above message!\n')
        else:    
            break


    # get user input for month (all, january, february, ... , june)
    while(True):
        if flag == 1: 
            break
        month = input('\n\nWhich month you wanna explore?!\n (jan, feb, mar, apr, may, june, or all)?!')
        month = month.lower().strip()
        if month == 'exit':
            flag = 1
            break
        if month not in months.keys():
            print('\nmonth name error !!')
            print('please enter the month as written in the above message!\n')
        else:    
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while (True):
        try:
            if flag == 1: 
                break
            day = input('\n\nWhich day you wanna explore?! please type your response as an integer\n (Monday = 0)?! or all')
            day = day.lower().strip()
            if day == 'exit':
                flag = 1
                break
            if day != 'all':
                if int(day) in range(0, 7):
                    break
                else:
                    continue
            else:
                break
        except:
            print('\nPlease enter a valid number, or enter "all" if you want the filter to select all days of the week\n')

        print('-'*40)
#     print(city, month, day)
    if flag == 1:
        return 1, 1, 1, 1
    else:
        print('\n\n\nPlease waite a while ^.^!\n\n')
        return city, month, day, flag
        
        
        
def preprocessing(df, city):
    # Convert the start and end time into datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # Extract the month from the start date
    df['month'] = df['Start Time'].dt.month

    # Extract the day number from the start time
    df['day'] = df['Start Time'].dt.dayofweek

    # Extract the hour from the start time
    df['hour'] = df['Start Time'].dt.hour
    
#     # Extract the year from the birth year
#     if city in ['chicago', 'new york city']:
#         df['Birth Year'] = df['Birth Year'].dt.year

#     print('preprocessing done')




def check_function():
    flag = 0
    while(True):
        if flag == 1:
            break
        try:
            show_ = input('wanna continue?! type "yes" or "no"!\n\n').lower().strip()
        except:
            print('Exception!! Invalid response\n\n')
            continue
        if ((show_ != 'yes') & (show_ != 'no')):
            print('you entered invalid respone!\n\n')
        elif ((show_ == 'yes') | (show_ == 'no')):
            flag = 1
        if show_ == 'no':
            print('It seems that you wanna leave! Thnaks for your time! ^.^!\n\n')
            break
    return show_, flag



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
    df = pd.read_csv(CITY_DATA[city])
    preprocessing(df, city)
    if month != 'all':
        df = df[df['month'] == months[month]]
    if day != 'all':
        df = df[df['day'] == int(day)]
#     print('Data loading done')
    print('='*70)
    print('If you wanna explore the data frame just type "yes" or "no"!\n\n')
    start = 0
    for i in range(len(df)):
        show_, flag = check_function()
        if show_ == 'yes':
            if len(df.iloc[start:]) > 5:
                print(df.iloc[start:start+5])
                start +=5
            else: 
                print(df.iloc[start:])
        elif show_ == 'no': 
    #         print('For loop break')
            break
    
    return df
    


def most_popular(df_name, df, feature):
    # The most popular feature
    most_popular = pd.value_counts(df[feature].values.flatten()).sort_values(ascending = False)
    
    if feature == 'day':
        print('\nFor '+df_name+' the most popular ' + feature +' is: ', days[most_popular.index[0]])
    else:
        print('\nFor '+df_name+', the most popular ' + feature +' is: ', most_popular.index[0])
    print('count is:', most_popular.iloc[0], end ='\n\n')    



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n--> Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_popular('DF', df, 'month')

    # display the most common day of week
    most_popular('DF', df, 'day')

    # display the most common start hour
    most_popular('DF', df, 'hour')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*70) 



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n--> Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    # The most popular station at the start of the trip
    most_popular_start_city = pd.value_counts(df['Start Station'].values.flatten()).sort_values(ascending = False)

    print('The most popular start station is: ', most_popular_start_city.index[0])
    print('Count is:', most_popular_start_city[1], end='\n\n')

    # display most commonly used end station
    # The most popular station at the end of the trip
    most_popular_end_city = pd.value_counts(df['End Station'].values.flatten()).sort_values(ascending = False)

    print('The most popular end station is: ', most_popular_end_city.index[0])
    print('Count is:', most_popular_end_city[1], end='\n\n')


    # display most frequent combination of start station and end station trip
    # Most popular trips data frame
    most_popular_trip_df = df[df.duplicated(subset = ['Start Station', 'End Station'])]

    # Most popular trips count
    most_popular_trip_count = pd.value_counts(most_popular_trip_df[['Start Station', 'End Station']].values.flatten()).sort_values(ascending = False)

    # Most popular trip
    print('The most popular trip is: ',most_popular_trip_count.index[0])
    print('The count is: ',most_popular_trip_count[1], end='\n\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*70)
    



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n--> Calculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The total travel time is: ', df['Trip Duration'].sum())
    
    # display mean travel time
    print('The mean travel time is: ', df['Trip Duration'].mean())
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*70)
    
    


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\n--> Calculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    pd.value_counts(df['User Type'].values.flatten())

    # Display counts of gender
    if city in ['chicago', 'new york city']:
        pd.value_counts(df['Gender'].values.flatten())
    

    # Display earliest, most recent, and most common year of birth
    if city in ['chicago', 'new york city']:
        print('The earliest year of bearth is: ', int(df['Birth Year'].min()))
        print('The most recent year of bearth is: ', int(df['Birth Year'].max()))
        most_common = pd.value_counts(df['Birth Year'].values.flatten()).sort_values(ascending = False).index[0]
        print('The most commomn year of bearth is: ', most_common)
    else:
        print('DF has no gender or birth year column')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*70)
    

    

# Main program
def main():
    while True:
        city, month, day, flag = get_filters()
        if flag != 1:
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df, city)
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                print('\nThanks.. We wanna see you again ^.^!')
                break
            
        else:
            print('='*70, end = '\n')
            print('It looks like you terminated the process. Thanks for your time!')
            print('='*70)
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                print('\nThanks.. We wanna see you again ^.^!')
                break
        


if __name__ == "__main__":
	main()
