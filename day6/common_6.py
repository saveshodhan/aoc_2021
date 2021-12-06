# AOC 2021 - day 5 #

from copy import deepcopy


def parse_input(input_file):
    points = list(map(int, open(input_file).read().split(",")))
    return points


def dec_all(d, reset_val, new_val):
    """Decrement all values.

    If we have an input list like [3, 4, 3, 2, 1], then in the next step we should
    decrement all values by 1. This would reesult in [2, 3, 2, 1, 0].

    If we continue to have a list, it increases the memory and hangs my terminal. So what
    I did is to have a dict with keys from 0 to max(input list), and their values set to 0.
    Then, we call `init_dict` with this input list and increment all keys present in the
    input list with 1. Thus, the above list will produce: {0: 0, 1: 1, 2: 1, 3: 2, 4: 1}.
    Note that the dict values indicate how many of them are in the list.

    Also, mentioned above - "decrement all values by 1" is same as saying that add the value
    at nth position in the dict to the value at n-1th position and reset the value at nth
    position to 0.
    In the next iteration, where we have to reduce each entry by 1, we just update the
    relevant key accordingly. For e.g., consider the first value - 3. It shoud become 2. In
    the dict context, what we do is `d[3-1] += d[3]` and then `d[3] = 0`. This way, if there
    are 2 entries with value 3, then d[3] would be 2. Because all of then have to be
    converted to 2, we just do `d[3-1] += 2`.

    But there's a catch - whenever a value becomes 0, in the next iteration it should
    become 6 (as per the AoC rule) and a new key should be added with value 8. To cater
    this, we have an index for -1. After updating all entries, if there are any entries
    for -1 (meaning there were 0s which got shifted while doing `d[n-1] += d[n]`) then we
    simple add those many entries (`d[-1]`) to d[6] and d[8] (we take these as variables
    because you never know what comes in part 2). And of course, reset d[-1] as well.
    And the best part is that we'll never get KeyError because the keys in the dict are
    actually counters in the input list (which will never exceed 8 in this case), and the
    count of those counters in the input list are the values in the dict!
    And we've already made dict using `range(-1, 8+1)`

    Another catch - because we're using a dict - which is mutable - it would cause the
    same dict object to be updated that is being iterated on. That's why we use `deepcopy`.
    """
    for k, v in deepcopy(d).items():
        if k == -1:
            continue
        else:
            d[k-1] += v
        d[k] = 0
    d[new_val] += d[-1]
    d[reset_val] += d[-1]
    d[-1] = 0
    return d


def init_dict(points, max_val):
    d = {x: 0 for x in range(-1, max_val+1)}
    for k in points:
        d[k] += 1
    return d
