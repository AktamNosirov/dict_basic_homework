def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    
    
    return dict(zip(key,value))
l1=[1,2,3]
l2=["one","two","three"]

print(create_dictionary(l1,l2))