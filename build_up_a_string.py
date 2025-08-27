# URL: https://github.com/jayklarin/Developers.Institute.2025/blob/main/build_up_a_string.py

# suggestions for improvement:
# - Correct Conditional Flow: The most critical improvement is to place all the subsequent logic (printing
#   first/last characters, building the string character by character, and jumbling the string) inside the
#   else block. This ensures that these operations only execute when the string is exactly 10 characters,
#   as explicitly stated in the instruction: "If the string is exactly 10 characters, print: 'Perfect string'
#   and proceed to the next steps." Currently, the code attempts to execute these steps regardless of string
#   length, leading to a IndexError if an empty string is entered, or incorrect behavior for strings that are
#   too short/long.

# - Improve Print Statement Formatting: Standardize the use of newlines (\n). While the current use is functional,
#   consider using print() for blank lines consistently or include \n within the string. Also, correct the typo
#   charcter to character in the print statements for better professionalism.
# - Enhanced User Experience (Optional but Recommended): Although not explicitly required, for practical
#   applications, you could wrap the input and length validation in a while loop. This would allow the user
#   to re-enter a string until it meets the 10-character requirement, rather than the program just completing
#   after a single incorrect attempt.
# Brief justification:

# - correctness: The code scores low on correctness (30%) primarily because it fails to adhere to a fundamental
#   requirement related to conditional logic, which is a core learning objective. The instructions clearly state:
#   'If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.' However,
#   the code proceeds with steps 3, 4, and 5 (printing first/last characters, building character by character,
#   and jumbling) unconditionally, even if the string is not 10 characters long. This leads to a critical
#   functional bug: if the user enters an empty string (which falls under 'less than 10 characters'), the code
#   will crash with an IndexError when attempting to access my_string[0] or my_string[-1]. While the individual
#   operations (slicing, looping, shuffling) are correctly implemented in isolation, their placement outside
#   the appropriate conditional block fundamentally breaks the intended program flow and error handling.
# - readability: The code has good readability (80%). Variable names (my_string, my_string_len) are clear
#   and descriptive. The overall structure is straightforward and easy to follow. The comments for the 'Jumble'
#   section are helpful. Minor deductions are for inconsistent newline handling in print statements (sometimes \n,
#   sometimes a separate print()) and a small typo (charcter), which could be easily fixed.
# - performance: The code demonstrates excellent performance (100%) for the given task. It involves basic string
#   manipulations, a single loop over a small string (ideally 10 characters), and standard library functions
#   (len(), string slicing, list(), random.shuffle(), join()). All these operations are highly efficient for
#   the expected input size, and there are no evident performance bottlenecks or inefficient algorithms.
# - security: The code is secure (100%) within the context of the problem. It handles user input as a plain string
#   and does not attempt to evaluate it or perform any operations that could lead to code injection or other
#   vulnerabilities. It uses the standard random module, which is safe. There are no file I/O, network operations,
#   or any privileged system interactions that could pose a security risk.



import random

def build_up_a_string():
    my_string = input("Type a string that is exactly 10 characters long: ")
    my_string_len = len(my_string)

    if my_string_len > 10:
        print("String too long.")
        return
    elif my_string_len < 10:
        print("String not long enough.")
        return
    else:
        print("Perfect string.\n")

        # Safe to access characters because length is exactly 10
        print("The first character in my string is", my_string[0])
        print("The last character in my string is", my_string[-1])
        print()

        for i in range(1, my_string_len + 1):
            print(my_string[:i])

        chars = list(my_string)           # turn string into list
        random.shuffle(chars)             # shuffle the list
        jumbled = ''.join(chars)          # rejoin into string
        print("\nJumbled string:", jumbled)

build_up_a_string()
