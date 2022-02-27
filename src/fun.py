def decimal(string):

    """Takes a string and returns a float"""    

    s = string.replace(',', '.')
    s = float(s)
    
    return s

def integer(string):

    """Takes a string and returns an integer""" 

    s = string.replace('.', '')
    s = int(s)

    return s