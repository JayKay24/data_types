def data_type(a_value):
    """
    This function takes in one argument and returns a value
    based on the type of the argument.
    """
    if a_value is None:
        return "no value"
    elif type(a_value) is str:
        # Return the strings length.
        return len(a_value)
    elif type(a_value) is bool:
        # Return the boolean.
        return a_value
    elif type(a_value) is int:
        if a_value < 100:
            return 'less than 100'
        elif a_value > 100:
            return 'more than 100'
        else:
            return 'equal to 100'
    elif type(a_value) is list:
        # The third item is available.
        if len(a_value) >= 3:
            return a_value[2]
        else:
            return None