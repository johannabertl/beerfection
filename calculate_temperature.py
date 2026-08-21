def lookup_temp(beer_type):
    """
    This function looks up the temperature for the given beer type.
    """
    mapping = {
        "lager": 7,
        "IPA": 9,
        "NEIPA": 9
    }
    return mapping.get(beer_type, "No result")

print(lookup_temp("lager"))