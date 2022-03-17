#! /usr/bin/python3

# Implementation of Matt Parker's "Shank Bot" from Numberphile.

# shank function as seen with long division algoithm
def shank_v1(n : int) -> int:
    
    # log of remainders las long division continues
    remainders = []

    # initial dividend (set to 1 because of the reciprocal)
    div = 1

    # loop unil repetition is found
    while True:

        # append the last remainder
        remainders.append(div)

        # do one step of long division
        div = (div * 10) % n

        # if there is a repeat, show the length, otherwise continue
        try:
            return len(remainders) - remainders.index(div)
        except ValueError:
            pass