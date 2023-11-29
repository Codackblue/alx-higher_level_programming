#!/usr/bin/python3

"""Print the numbers from 1 to 100 separated by a space.
  For multiples of three, print Fizz instead of the number
  For multiples of five, print Buzz instead of the number.
  For multiples of three and five, print FizzBuzz instead of the number.
  """


def fizzbuzz():
    for fnum in range(1, 101):
        if fnum % 3 == 0 and fnum % 5 == 0:
            print("FizzBuzz ", end="")
        elif fnum % 3 == 0:
            print("Fizz ", end="")
        elif fnum % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(fnum), end="")
