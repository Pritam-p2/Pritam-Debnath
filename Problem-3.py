'''
Problem-3: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
  Output: (examples)
    1) input a = 1, then output : 1
    2) input a = 2, then output : 1
    3) input a = 3, then output : 1, 3, 5
    4) input a = 4, then output : 1, 3, 5
    5) input a = 5, then output : 1, 3, 5, 7, 9
    6) input a = 6, then output : 1, 3, 5, 7, 9
    .
    .
    7) input a = x, then output : 1, 3, 5, 7, .......

'''

def produce_odd_number_series(length):
    list_of_odd_nos = range(1,2*length,2)
    buffer = ''
    for items in list_of_odd_nos:
        buffer = buffer + str(items)+ ', '
    return buffer[0:len(buffer)-2]    


def generate_series(a):
    try:
        if a < 1 or not isinstance(a,int):
            return 'Invalid Input'
        if a % 2==0:
            a = a-1
        return produce_odd_number_series(a)
    except Exception as e:
        return str(e)

print(generate_series(5))
print(generate_series(6))