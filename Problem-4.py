'''
Problem-4: Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
  (examples)
  input: [1,2,8,9,12,46,76,82,15,20,30]
  Output: 
    {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
'''

def find_total_number_of_multiples(input):
    try:
        dividers = [1,2,3,4,5,6,7,8,9]

        count_of_dividers_divided = {}

        for divider in dividers:
            for item in input:
                if item % divider == 0:
                    if divider not in count_of_dividers_divided:
                        count_of_dividers_divided[divider]=1
                    else:
                        count_of_dividers_divided[divider] =count_of_dividers_divided[divider]+1 
    except Exception as e:
        return str(e)
    return count_of_dividers_divided

print(find_total_number_of_multiples([1,2,8,9,12,46,76,82,15,20,30]))                