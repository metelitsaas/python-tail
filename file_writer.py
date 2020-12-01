import random
import time

FILE_NAME = 'test_file'


def main():

    i = 0
    while True:
        file = open(FILE_NAME, 'a')
        file.write('%(i)s_test_string\n' % {'i': i})
        file.close()
        i += 1
        time.sleep(random.uniform(0, 1))


if __name__ == '__main__':
    main()
