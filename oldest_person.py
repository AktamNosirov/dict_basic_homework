def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    l1=people.keys()
    l2=people.values()
    a=dict(zip(l2,l1))
    return a[max(people.values())]
       
       
    
people={"Aktam":27, "Doston": 22, "O'tkir" :37, "Muhriddin":30 }
print(oldest(people))