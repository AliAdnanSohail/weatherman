import sys

import file_handler
import highest_value_calculator
import average_calculator
import bar_chart_generator


def main():
    file_path = sys.argv[1]
    zip_name = 'weatherfiles.zip'
    file_handler.extract_file(file_path, zip_name)
    print("Files extracted to /" + file_path)

    operation_indexes = [i for i in [2, 4, 6] if i+1 < len(sys.argv)]
    for operation_index in operation_indexes:
        duration_index = operation_index + 1
        operation = sys.argv[operation_index]
        duration = sys.argv[duration_index]
        generate_report(file_path, operation, duration)


def generate_report(file_path, operation, duration):
    if operation == '-e':
        highest_value_calculator.display_highest(file_path, duration)
    elif operation == '-a':
        average_calculator.display_average(file_path, duration)
    elif operation == '-c':
        bar_chart_generator.display_bar_chart(file_path, duration)
    else:
        print('Invalid input {operation}'.format(operation=operation))


main()
