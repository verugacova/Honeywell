
def taskOne():

    i = 1

    while i <= 100:
        if i%2 == 0 and i%3 == 0:
            print("twothree")
        elif i%2 == 0:
            print("two")
        elif i%3 == 0:
            print("three")
        else:
            print(i)
        i += 1

taskOne()
    