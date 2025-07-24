from datetime import datetime,timedelta


def calculate_future_date():

    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")



def display_current_datetime():
    date_now = datetime.now()
    current_date = date_now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
    return current_date

display_current_datetime()
calculate_future_date()