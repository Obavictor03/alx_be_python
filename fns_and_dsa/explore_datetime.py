from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date =current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date)

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))

    current_date = datetime.now()

    future_date = current_date + timedelta(days=number_of_days)

    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

display_current_datetime()
calculate_future_date()