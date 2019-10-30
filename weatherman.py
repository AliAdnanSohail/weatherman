import sys

import file_handling
import display_highest
import display_average
import display_bar_chart


def main():
    path = file_handling.extract_file(sys.argv[1])
    print("Files extracted to /" + path)

    index = [i for i in [2, 4, 6] if i+1 < len(sys.argv)]
    for i in index:
        generate_report(path, sys.argv[i], sys.argv[i+1])


def generate_report(path, operation, _input):
    if operation == '-e':
        display_highest.display_highest_values(path, _input)
    elif operation == '-a':
        display_average.display_average_values(path, _input)
    elif operation == '-c':
        display_bar_chart.display_bar_chart(path, _input)
    else:
        print("Invalid input " + _input)


main()
