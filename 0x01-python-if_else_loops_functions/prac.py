def uppercase(str):
    """
    uppercase() - prints a string in uppercase
    str - parameter passed
    """
    for i in str:
	    print("{}".format(chr(ord(i) - 32)) if ord('a') <= ord(i) <= ord('z') else "{}".format(i), end="\n" if i == str[-1] else "")
