import sys

from file_handler.zip_file_processor import ZipFileProcessor
from values_calculator.highest_value_calculator import HighestValueCalculator
from values_calculator.average_calculator import AverageCalculator
from values_calculator.bar_chart_generator import BarChartGenerator


def main():
    extract_to_path = sys.argv[1]
    zip_name = 'weatherfiles.zip'
    directory_name = 'weatherfiles'
    zip_file = ZipFileProcessor(extract_to_path, zip_name, directory_name)
    zip_file.extract_files()
    print("Files extracted to /" + zip_file.path)

    operation_indexes = [i for i in [2, 4, 6] if i+1 < len(sys.argv)]
    for operation_index in operation_indexes:
        duration_index = operation_index + 1
        operation = sys.argv[operation_index]
        duration = sys.argv[duration_index]
        generate_report(zip_file, operation, duration)


def generate_report(zip_file, operation, duration):
    if operation == '-e':
        HighestValueCalculator(zip_file_ref=zip_file, duration=duration).display_highest()
    elif operation == '-a':
        AverageCalculator(zip_file_ref=zip_file, duration=duration).display_average()
    elif operation == '-c':
        BarChartGenerator(zip_file_ref=zip_file, duration=duration).display_bar_chart()
    else:
        print('Invalid input {operation}'.format(operation=operation))


main()
