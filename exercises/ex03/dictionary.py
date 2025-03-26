__author__: str = "730559966"


def invert(given: dict[str, str]) -> dict[str, str]:
    """Takes a given dict and inverts the keys and their associated values."""
    inverted: dict[str, str] = {}
    for key in given:
        inv_key: str = given[key]
        inv_value: str = key
        # switches keys and values
        if inv_key in inverted:
            raise KeyError("Cannot have duplicate keys")
        # establishes KeyError
        inverted[inv_key] = inv_value
        # binds value to key when reversed
    return inverted


def count(provided: list[str]) -> dict[str, int]:
    """Returns a dict where the values represent how many times key appeared in list"""
    count_dict: dict[str, int] = {}
    i: int = 0
    while i < len(provided):
        if provided[i] in count_dict:
            count_dict[provided[i]] += 1
        else:
            count_dict[provided[i]] = 1
        i += 1
    return count_dict


def favorite_color(input: dict[str, str]) -> str:
    """Returns color that appears the most"""
    fav_color: list[str] = []
    for key in input:
        fav_color.append(input[key])
        # turns dict values into list usable by count function
    color_dict: dict[str, int] = count(fav_color)
    # uses count to make dict
    i: int = 0
    color: str = ""
    for key in color_dict:
        if color_dict[key] > i:
            i = color_dict[key]
            color = key
    # finds highest value and reassigns color to the key for that value
    return color


def bin_len(bin_list: list[str]) -> dict[int, set[str]]:
    """produces dict of number keys with values of words at that len"""
    bin_dict: dict[int, set[str]] = {}
    for word in bin_list:
        if len(word) in bin_dict:
            bin_dict[len(word)].add(word)
            # adds word to set
        else:
            bin_dict[len(word)] = set()
            # establishes number key with empty set
            bin_dict[len(word)].add(word)
            # adds word to set
    return bin_dict
