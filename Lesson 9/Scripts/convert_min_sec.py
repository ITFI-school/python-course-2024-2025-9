def convert_to_minutes(num_hours):
    """ (int) -> int
    Return the number of minutes there are in num_hours hours
    Precondition: num_hours >= 0, otherwise -> 0
    >>> convert_to_minutes(2)
    120
    >>> convert_to_minutes(-2)
    0
    """
    if num_hours < 0:
        return 0
    minutes = int(num_hours) * 60
    return minutes

def convert_to_seconds(num_hours):
    """ (int) -> int
    Return the number of seconds there are in num_hours hours
    Precondition: num_hours >= 0, otherwise -> 0
    >>> convert_to_minutes(2)
    7200
    >>> convert_to_minutes(-2)
    0
    """
    minutes = convert_to_minutes(num_hours)
    seconds = minutes * 60
    return seconds

seconds = convert_to_seconds(2)