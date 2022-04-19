def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    dict={ "Letters":0 , "Digits":0}
    index=0
    for i in range(len(txt)):
        if txt[index].isalpha() :
            dict["Letters"]+=1
        if txt[index].isdigit() :
            dict["Digits"]+=1    
        index+=1     
    return dict
print(count_all("rg git 546"))