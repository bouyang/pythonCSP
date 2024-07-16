def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and (len([num for num in pin if num in '1234567890']) == 4 or len([num for num in pin if num in '1234567890']) == 6)