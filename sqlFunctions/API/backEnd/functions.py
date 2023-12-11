import random
from datetime import datetime





def generateDate():
    current_time = datetime.now()
    return current_time.strftime("%Y%m%d%H%M%S")
     

def generate_unique_id(random_string):
    random_string += generateDate()
    # Get the hash value of the random string
    hash_value = hash(random_string)
    
    # Take the absolute value and limit the length to 10 digits
    unique_id = str(abs(hash_value) % (10 ** 10))
    
    return unique_id[:9]


from datetime import datetime, timedelta

def calculate_future_time(minutes):
    # Get the current datetime
    current_time = datetime.now()

    # Calculate future time by adding minutes
    future_time = current_time + timedelta(minutes=minutes)

    # Format the future time as a string in the desired format
    formatted_future_time = future_time.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_future_time



