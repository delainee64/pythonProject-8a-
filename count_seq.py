# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 02/25/2023
# Description: Write a generator function named count_seq that doesn't require any arguments and generates
# a sequence that starts like this: 2, 12, 1112, 3112, 132112, 1113122112, 311311222112, 13211321322112.

def count_seq():
    """A generator function that creates a sequence."""
    num = "2"  # String instead of integer.
    while True:
        yield int(num)
        next_num = ""
        while len(num) > 0:
            value = num[0]
            count = 0
            while len(num) > 0 and num[0] == value:
                count += 1
                num = num[1:]  # Removes the first number.
            next_num += "{}{}".format(count, value)  # Replaces the num with the next value.
        num = next_num


# generate = count_seq()
# for ind in range(20):
#     print(next(generate))
