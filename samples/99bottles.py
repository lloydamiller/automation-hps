# this script will print out the lyrics to 99 bottles of beer

# We are counting down from 99 to 0, so we set our variable to 99
number_of_bottles = 99

while number_of_bottles >= 0:
    # In the first line of each verse, we want to test if the number of bottles is greater than 1 (plural), equal to 1 (singular), or
    # less than 1 (the last line of the song) and print the appropriate statement
    if number_of_bottles > 1:
        print(f"{number_of_bottles} bottles of beer on the wall, {number_of_bottles} bottles of beer.")
    elif number_of_bottles == 1:
        print(f"{number_of_bottles} bottle of beer on the wall, {number_of_bottles} bottle of beer.")
    else:
        # if the number of bottles is not greater than 1, and it does not equal 1, then the first time this code runs
        # number_of_bottles will equal 0 (the last line of the song) so you can just print out the last line and then break the loop
        # which prevents the else statement at the end from running. The \n creates a new line in the console.
        print("""No more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, 99 bottles of beer on the wall.""")
        break

    # this code reduces the number of bottles by one each time the loop iterates so it counts down by 1 each time it runs
    number_of_bottles -= 1

    # this tests if bottles equals any number but one. If you make the test affirmative (e.g. number_of_bottles == 1)
    # then you can flip the phrases.
    if number_of_bottles != 1:
        print(f"Take one down, pass it around, {number_of_bottles} bottles of beer on the wall.")
    else:
        print(f"Take one down, pass it around, {number_of_bottles} bottle of beer on the wall.")
