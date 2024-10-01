
FILE_SIZE_UNITS = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB']

FILE_SIZE_UNITS_TO_BYTES = list(map(lambda v: int(1024 ** v), 
                                    range(len(FILE_SIZE_UNITS))))

FILE_SIZE_DECIMAL_UNITS = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']

FILE_SIZE_DECIMAL_UNITS_TO_BYTES = list(map(lambda v: int(1000 ** v),
                                            range(len(FILE_SIZE_DECIMAL_UNITS))))

assert len(FILE_SIZE_UNITS) == len(FILE_SIZE_UNITS_TO_BYTES)
assert len(FILE_SIZE_DECIMAL_UNITS) == len(FILE_SIZE_DECIMAL_UNITS_TO_BYTES)
assert len(FILE_SIZE_UNITS) == len(FILE_SIZE_DECIMAL_UNITS)


def beautify_size_bytes(bytes: int, *, decimal=False, force_int=False) -> str:
    """
    Convert a byte count into a human-readable string.

    This function takes an integer representing the number of bytes and returns
    a string representing the size in a human-readable format. The format can
    be either binary (default) or decimal, depending on the value of the 
    `decimal` parameter.

    Parameters:
    bytes (int): The number of bytes to be converted. Must be an integer.
    decimal (bool, optional): If True, use decimal units (KB, MB, GB, etc.). If False (default), use binary units (KiB, MiB, GiB, etc.).
    force_int (bool, optional): If True and the number is an integer, display it without decimal dot. Otherwise display it as a float.

    Returns:
    str: A string representing the size in a human-readable format.
    """
    assert int(bytes) == bytes, 'number of bytes must be an integer'
    units = FILE_SIZE_DECIMAL_UNITS if decimal else FILE_SIZE_UNITS
    unit_to_bytes = (FILE_SIZE_DECIMAL_UNITS_TO_BYTES if decimal 
                        else FILE_SIZE_UNITS_TO_BYTES)
    if bytes < 0:
        return '-{}'.format(beautify_size_bytes(
            int(-bytes), decimal=decimal, force_int=force_int))
    if bytes >= unit_to_bytes[1]:
        for i in range(max(0, len(units) - 1)):
            if bytes < unit_to_bytes[i + 1]:
                size = unit_to_bytes[i]
                unit = units[i]
                return '{} {}'.format(
                    beautify_number(bytes / size, force_int=force_int), unit)
    return '{} B'.format(beautify_number(bytes, force_int=True))


def beautify_number(number: float | int, *, force_int):
    assert not isinstance(number, float) or not isinstance(number, int), \
        'number must be an integer or a floating-point number'
    if force_int:
        number_int = int(number)
        if number_int == number:
            return '{:_d}'.format(number_int)
    # number must be a floating-point number
    return '{:.2f}'.format(number)
