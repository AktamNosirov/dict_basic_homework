def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    a=enumerate(cities)
    return list(a)
cities=["Samarkand","Tashkent"]
print(cities_dict(cities))

