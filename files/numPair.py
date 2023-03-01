print("""
Number Factorizer
-----------------
List all the factors of a number
(0 to quit)

""")


def list_factors(num):
    """Returns a list of factors for 'num'"""
    all_solutions = []
    dividend = 1

    absolute_number = abs(num)
    while True:
        if dividend > absolute_number:
            break
        elif absolute_number % dividend == 0:
            all_solutions.append(dividend)
        dividend += 1

    # Create pairs of solutions
    all_pairs = []
    interator = 1
    for i in range(0, len(all_solutions)):
        if i == (len(all_solutions) // 2):  # ADD "and (len(all_solutions) % 2) == 0 to list backwards too"
            if (len(all_solutions) % 2) != 0:  # Odd number of solutions
                middle_pair = [all_solutions[-interator], all_solutions[-interator]]
                all_pairs.append(middle_pair)

            break
        pair = [all_solutions[i], all_solutions[-interator]]
        all_pairs.append(pair)
        interator += 1

    return {'pairs': all_pairs, 'solutions': all_solutions}


while True:
    user_input = int(input('> '))
    factors = list_factors(user_input)

    if user_input < 0:
        print("Pairs: +- " + str(factors['pairs']))
        print("Solutions: +- " + str(factors['solutions']))
        print("Best Solution: +- " + str(factors['pairs'][-1]))
    elif user_input > 0:
        print("Pairs: " + str(factors['pairs']))
        print("Solutions: " + str(factors['solutions']))
        print("Best Solution: " + str(factors['pairs'][-1]))
    else:  # user_input == 0
        break

    print() # Blank line
