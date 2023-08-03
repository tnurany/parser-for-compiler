import sys

# Define a global variable to keep track of the current position in the input string
pos = 0


# Define a function to check if the current character matches the expected character
def match(expected):
    global pos
    if pos < len(input_str) and input_str[pos] == expected:
        pos += 1
        return True
    return False


# Define a function for each non-terminal in the grammar
def parse_S():
    parse_E()


def parse_E():
    if match("("):
        parse_E_prime()
    elif match("num"):
        return
    else:
        reject()


def parse_E_prime():
    if match("+") or match("-") or match("*") or match("/"):
        parse_E()
        parse_E()
        if not match(")"):
            reject()
    else:
        reject()


# Define a function to handle rejection
def reject():
    print("Reject")
    sys.exit()


# Define the main parsing function
def parse(input_string):
    global pos, input_str
    input_list = []
    space_removed = input_string.replace(" ", "")
    i = 0
    while i < (len(space_removed)):
        if space_removed[i] == 'n':
            input_list.append("num")
            i += 2
        else:
            input_list.append(space_removed[i])

        i += 1

    input_str = input_list
    pos = 0
    parse_S()
    if pos == (len(input_str)):
        print("Accept")
    else:
        reject()


# Define the main function to read input from standard input
def main(argv):
    input_str = ""
    for line in sys.stdin:
        input_str += line.strip() + " "
    parse(input_str)


if __name__ == '__main__':
    main(sys.argv)
