# Weatherman Report Generator

## Prerequisite
  - Python3

## Steps to create report
  - Clone the project
  - Run following commands according to required report

## Commands
  - To display highest temperature, lowest temperature and humidity for a given year
    ```sh 
    python3 weatherman.py path/to/extract -e 2009
    ```
  - To display average highest temperature, average lowest temperature, average mean humidity for a given month
    ```sh 
    python3 weatherman.py path/to/extract -a 2009/05
    ```
  - To draw horizontal bar charts temp and humidity for a given month
    ```sh 
    python3 weatherman.py path/to/extract -c 2009/05
    ```
  - To generate multiple reports
    ```sh 
    python3 weatherman.py /path/to/extract -c 2011/03 -a 2011/3 -e 2011
    ```
