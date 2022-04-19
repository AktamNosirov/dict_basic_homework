def last_item():
    """
    Given a dictionary, Return last item value.
    """
    data = {'a': 1, 'b': 2}
    return list(data.values())[-1]
print(last_item())