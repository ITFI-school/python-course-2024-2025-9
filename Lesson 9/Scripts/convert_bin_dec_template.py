def to_binary(dec_num):
    """
    (int) -> str
    Return the binary representation of a dec_num
    Preconditon: dec_num >= 0, if violated -> ""
    >>> to_binary(23)
    '10111'
    >>> to_binary(-3)
    ''
    """
    if dec_num < 0:
        return ""
    str_bin = ""
    # write your code here:

    return str_bin

def to_decimal(str_bin):
    """
    (str) -> int
    Return the decimal equivalent of str_bin containing '0's and '1's
    Precondition: if str_bin contains the characters other than '0' and '1' -> 0
    >>> to_decimal("10111")
    23
    >>> to_decimal("10112")
    ''
    """
    if len(str_bin)==0 or set(str_bin)!={'0','1'}:     
        return 0
    result = 0
    # write your code here:

    return result
