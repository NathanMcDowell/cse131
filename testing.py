# def reverse_string_loop(sentence):
#     for i in range(len(sentence)-1, -1, -1):
#         print(sentence[i], end='')

# def reverse_string_recursion(sentence, index):
#     if index == 0:
#         return sentence[index]
#     return sentence[index] + reverse_string_recursion(sentence, index -1)

def get_integer():
    while True:
        integer = input('Input an positive integer: ')
        try:
            integer = int(integer)
            if integer >= 0:
                return integer
            else:
                print('Not a positive integer')
        except ValueError:
            print('Not an integer')

def convert_integer(int):
    '''Call functions to convert number to binary, octal, and hexadecimal'''
    return convert_to_binary(int), convert_to_octal(int), convert_to_hex(int)

def convert_to_binary(int):
    '''Convert an integer into a binary string.
    Return a binary string'''
    return '0b001101101'

def convert_to_octal(int):
    '''Convert an integer into an octal string.
    Return a octal string'''
    return '0o12353'

def convert_to_hex(int):
    '''Convert an integer into a hex string.
    Return a hex string'''
    return '0xB3'

def display(int, binary, octal, hex):
    '''Display number and it's conversions.'''
    print(f'Integer: {int}')
    print(f'Binary: {binary}')
    print(f'Octal: {octal}')
    print(f'Hexadecimal: {hex}')


def main():
    '''Runs the program.'''
    # int = get_integer()
    # binary, octal, hex = convert_integer(int)
    # display(int, binary, octal, hex)
    get_integer()

main()




'''
INPUT: numbers_list 

// Keep looping until the entire list is one sorted sublist 

REPEAT 

    sublists ← empty list 

    current_sublist ← empty list 

    // Step 1: Break the list into ascending sublists 

    FOR i FROM 0 TO LENGTH(numbers_list)-1 

        IF current_sublist is empty 

            ADD numbers_list[i] to current_sublist 

        ELSE IF numbers_list[i] >= last element of current_sublist 

            // Still ascending, keep adding 

            ADD numbers_list[i] to current_sublist 

        ELSE 

            // Ascending order broke, start a new sublist 

            ADD current_sublist to sublists 

            current_sublist ← [numbers_list[i]] 

        END IF 

    END FOR 

    // Add the final sublist 

    ADD current_sublist to sublists 

    // Step 2: Merge adjacent sublists pairwise 

    merged_sublists ← empty list 

    index ← 0 

    WHILE index < LENGTH(sublists) 

        IF index = LENGTH(sublists) - 1 

            // Odd number of sublists, last one has no partner 

            ADD sublists[index] to merged_sublists 

        ELSE 

            // Merge two sorted sublists 

            merged ← MERGE(sublists[index], sublists[index + 1]) 

            ADD merged to merged_sublists 

        END IF 

        index ← index + 2 

    END WHILE 

    // Step 3: Flatten merged_sublists back into one list 

    numbers_list ← concatenation of all lists in merged_sublists 

UNTIL LENGTH(merged_sublists) = 1 

OUTPUT numbers_list 

// Helper function: merge two sorted lists 

FUNCTION MERGE(listA, listB) 

    result ← empty list 

    i ← 0 

    j ← 0 

    WHILE i < LENGTH(listA) AND j < LENGTH(listB) 

        IF listA[i] <= listB[j] 

            ADD listA[i] to result 

            i ← i + 1 

        ELSE 

            ADD listB[j] to result 

            j ← j + 1 

        END IF 

    END WHILE 

    // Add leftovers 

    WHILE i < LENGTH(listA) 

        ADD listA[i] to result 

        i ← i + 1 

    END WHILE 

    WHILE j < LENGTH(listB) 

        ADD listB[j] to result 

        j ← j + 1 

    END WHILE 

    RETURN result 

END FUNCTION 
'''