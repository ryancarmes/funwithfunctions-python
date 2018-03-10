def odd_even(a, b):
    for count in range(a, b):
        if count % 2 == 0:
            even = "Number is "
            even += str(count)
            print  even + ". " + "This is an even number."
        else:
            odd = "Number is "
            odd += str(count)
            print odd + ". " + "This is an odd number."

odd_even(1, 100)

def multiply(arr, num):
    for count in range(0, len(arr)):
      arr[count] *= num
    return arr

list = [2, 4, 10, 16]
print multiply(list, 5)

def layered_multiples(arr):
    new_array = []
    for x in arr:
        value_arr =  []        
        for i in range(0,x):
            value_arr.append(1)
        new_array.append(value_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x




