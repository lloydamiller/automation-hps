# this script will print out the lyrics to 99 bottles of beer

number_of_bottles = 99

while number_of_bottles >= 0:
    if number_of_bottles > 1:
        print(str(number_of_bottles) + " bottles of beer on the wall, " + str(number_of_bottles) + " bottles of beer.")
    number_of_bottles -= 1