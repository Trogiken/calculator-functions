print("""
X Factor Solver
---------------
When a == 1: b on top, c on bottom
When a > 1: b on top, (c * a) on bottom

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
    is_negative = False

    top_number = int(input('Top Number: '))
    bottom_number = int(input('Bottom Number: '))
    factors = list_factors(bottom_number)

    if bottom_number < 0:
        is_negative = True
        print(f"Pairs: +- {factors['pairs']}")
        print(f"Solutions: +- {factors['solutions']}")
    else:
        print(f"Pairs: {factors['pairs']}")
        print(f"Solutions: {factors['solutions']}")

    # Use pairs to test if they add together to get top_number
    # If negative do the same as in step one but have to make every number negative and positive

    print()  # Separate future inputs
