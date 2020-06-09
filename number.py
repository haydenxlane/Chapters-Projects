import time

def isNumberSorted(number):
    '''
    Checks if the number is sorted
    Converts number to string and then to list to sort it 
    Returns True if yes and False if not
    '''
    original_number = list(str(number))
    sorted_number = sorted(str(number))
    if original_number == sorted_number:
        return True
    else:
        return False

def main():
    possible_solutions = []
    scope_min = 372**2
    scope_max = 809**2
    scope = range(scope_min, scope_max + 1)

    for number in scope:
        #checks if the number is sorted
        if isNumberSorted(number):
            #sets the flag for counting pairs of numbers
            pairs = 0 
            #sets another flag for checking if the new pair is unique
            var = 0 
            for i in range(len(str(number)) - 1):
                if str(number)[i] == str(number)[i+1]:
                    #checks if the adjacent numbers are the same
                    #and if so, if the pair is unique
                    if int(str(number)[i]) != var:
                        var = int(str(number)[i])
                        pairs += 1
                        if pairs == 2:
                            possible_solutions.append(number)
        

    solution = len(possible_solutions)
    print("Chapter Two: Finding the numbers that meet the following criteria: ")
    time.sleep(1)
    print(" - Min number: 372**2 \n - Max number: 809**2")
    time.sleep(1)
    print(" - At least two pairs of adjacent numbers")
    time.sleep(1)
    print(" - Adjacent numbers can only grow or stay the same")
    time.sleep(1)
    print("Calculating...")
    time.sleep(3)
    solution_string = "In the scope from {0} to {1} we can find {2} numbers that meet the criteria".format(scope_min, scope_max, solution)
    print(solution_string)
    cont = input("Do you want to print the possible solutions? 'y' or 'n': ")
    if cont == 'y':
        print(possible_solutions)

if __name__ == '__main__':
    main()