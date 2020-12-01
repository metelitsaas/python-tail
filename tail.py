#!/usr/bin/python3
"""
Python3 script
"""

import os
import sys
import time
import argparse

SLEEP_PERIOD = 0.1  # time to sleep between file reading in seconds


class Tail:
    """
    Class of Python analog for linux tail function
    """
    def __init__(self, path, follow_flag=False, sleep_period=0.1):
        """
        :param path: path to the file
        :param follow_flag: file monitoring flag, default - False
        :param sleep_period: time to sleep between file reading in seconds, default - 0.1
        """
        self.path = path
        self.follow_flag = follow_flag
        self.sleep_period = sleep_period
        self.check_file()

    def run(self):
        """
        Run main body function
        """
        # Open file safely
        with open(self.path, 'r') as file:

            # Show N tail rows from file
            tail_data = self.standard_mode(file)
            self.print(tail_data)

            # If follow flag -f is on run file monitoring
            if self.follow_flag:
                while True:
                    follow_data = self.follow_mode(file, self.sleep_period)
                    self.print(follow_data)

    @staticmethod
    def standard_mode(file, lines_count=10):
        """
        Standard tail function realized by Exponential Search
        :param file: file to read
        :param lines_count: N lines in the end of the file to show, default - 10
        :return : lines from tail
        """
        # Result lines from tail
        result_lines = []

        # Increment for search implementation
        pos = lines_count + 1

        # Loop until find N line
        while len(result_lines) <= lines_count:

            # Moving cursor to find range
            try:
                file.seek(-pos, os.SEEK_END)

            # Handle exception when file is less than lines to return
            except IOError:
                file.seek(0)
                break

            # Write founded lines
            finally:
                result_lines = list(file)

            # Exponentially increase search range
            pos *= 2

        return result_lines[-lines_count:]

    @staticmethod
    def follow_mode(file, sleep_period):
        """
        File monitor tail function
        :param file: file to read
        :param sleep_period: time to sleep between file reading in seconds
        :return: new line in file
        """
        # Move cursor to the end of the file
        file.seek(0, os.SEEK_END)

        # Infinity loop
        while True:

            line = file.readline()
            # Sleep if there are no updates
            if not line:
                time.sleep(sleep_period)
                continue

            yield line

    @staticmethod
    def print(data):
        """
        Print data line by line
        :param data: data from file
        """
        for line in data:
            print(line, end='')

    def check_file(self):
        """
        File validity checks
        """
        # Check that file exists
        if not os.access(self.path, os.F_OK):
            raise Exception('File %s does not exist' % self.path)

        # Check that file is readable
        if not os.access(self.path, os.R_OK):
            raise Exception('File %s is not readable' % self.path)

        # Check that filename is not a directory
        if os.path.isdir(self.path):
            raise Exception('%s is a directory' % self.path)


def main():
    """
    Main script function
    """
    # Define parser
    parser = argparse.ArgumentParser(prog='%s' % os.path.basename(__file__),
                                     usage='%(prog)s [-f] path',
                                     description='Python analog for linux tail function, '
                                                 'Ctrl+C to exit')

    # Add parser arguments
    parser.add_argument('-f', action='store_true', help='file monitoring')
    parser.add_argument('path', metavar='path', type=str, help='path to file')

    # Parse arguments
    args = parser.parse_args()
    follow_flag = args.f  # -f file monitoring flag
    file_path = args.path  # path of the file

    # Create tail instance
    tail = Tail(file_path, follow_flag, SLEEP_PERIOD)

    # Run tail function
    try:
        tail.run()

    # Handle function stop
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)


if __name__ == '__main__':
    main()
