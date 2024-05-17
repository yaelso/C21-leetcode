def second_symbol(s, symbol):
    count = 0

    for idx, letter in enumerate(s):
        if letter == symbol:
            count += 1

            if count == 2:
                return idx

    return -1

# second_symbol('Hello world!!!','l') --> 3
# second_symbol('Hello world!!!', 'A') --> -1
