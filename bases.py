import string

def letter_from_num(num):
    """ Convert letter from number:
    input: int -- integer representation of number (in base 10)
    return: strings of letters """
    letters  ='abcdefghijklmnopqrstuvwxyz'
    return letters[num - 10]

def digit_from_letter(letter):
    """
    input: any letter
    return: int -- number representation of number (in base 10)
    handles digits from hexadecimal (base 16)
    handles digits from any base (2 up to 36)
    math function that calculate the number based on math conversion
    this calculate from the 36 letters -97 + 1
    """
    num = ord(letter) - 97 + 10
    return num

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: result is int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    result = 0
    # Loop through the enumeration
    # index and digit
    # create a helper function that handles hexadecimal digit_from_letter
    for index, digit in enumerate(digits):
        if digit.isdigit():
            digit_to_add = int(digit)
        else:
            digit_to_add = digit_from_letter(digit)
        # add them together on the result with the digital_to_add to the result
        result += digit_to_add
        if index is not len(digits) - 1:
            result *= base
        else:
            1
    # Return the result decimal digit
    return result

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    new_base_number = ''
    # encode helps me to make sure that we will work
    while number != 0:
        remainder = number % base
        number = number // base
        if (remainder >= 10 and base > 10):
            remainder = letter_from_num(remainder)
        else:
            remainder
        new_base_number += str(remainder)
    # Reverse
    new_base_number = new_base_number[::-1]
    return new_base_number