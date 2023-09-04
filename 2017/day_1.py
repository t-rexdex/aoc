import sys

"""Find the sum of all digits that match the next digit in the list.
The list is circular, so the digit after the last digit is the first
digit in the list
For Example:

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
"""


def catch_key_error(
    dictionary_to_test: dict[str, int], key_to_test: str
) -> dict[str, int]:
    try:
        dictionary_to_test[key_to_test] += 1
    except KeyError:
        dictionary_to_test[key_to_test] = 1

    return dictionary_to_test


def iterate_through_list(user_str: str) -> None:
    old_i = None
    counter = 0
    reference_dict: dict[str, int] = {}

    for i in user_str:
        if i == old_i:
            # print(f"matching number found {i} in position {counter-1} and {counter}")
            reference_dict = catch_key_error(reference_dict, i)

        elif i == user_str[0] and counter == 0:
            reference_dict = catch_key_error(reference_dict, i)

        counter += 1
        old_i = i
    return count_input_sum(reference_dict)


def count_input_sum(count_dict: dict[str, int]) -> None:
    for key in count_dict:
        count_dict.update({key: int(key) * count_dict[key]})

    print(
        f"The sum of your input with the conditions matched is: {sum(count_dict.values())}"
    )


def part_2(input_string):
    # Initialize the total sum to zero
    total_sum = 0

    # Calculate the length of the input string
    input_length = len(input_string)

    # Iterate over each digit in the input string
    for i in range(input_length):
        # Get the current digit and the digit halfway around the list
        current_digit = int(input_string[i])
        halfway_around_digit = int(input_string[(i + input_length // 2) % input_length])

        # If the digits match, add them to the total sum
        if current_digit == halfway_around_digit:
            total_sum += current_digit
    print(f"The answer to part 2 is: {total_sum}")


user_input = sys.argv[1]
# user_lst = user_input.split(",")

iterate_through_list(user_input)

part_2(user_input)
