def odd_even():
    for count in range(1, 2001):
        if count % 2 == 0:
            even = "Number is "
            even += str(count)
            print  even + ". " + "This is an even number."
        else:
            odd = "Number is "
            odd += str(count)
            print odd + ". " + "This is an odd number."

odd_even()