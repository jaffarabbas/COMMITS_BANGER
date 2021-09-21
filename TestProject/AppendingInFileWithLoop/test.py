import os
import time


# function to insert values in file
def InsertIntoFile(count):
    file = open('tester.txt', 'a')
    print(count)
    file.write(str(count) + "\n")
    file.close()


# function to clear file
def ClearFile():
    count = 0
    file = open('tester.txt', 'r')
    # read file
    readFile = file.read()
    # check line breaks in a file
    checkFile = readFile.split('\n')
    # count each line
    for i in checkFile:
        if i:
            count += 1
    # clear file when it hit given range
    print('Count : ', count)
    if count >= 50:
        tempFile = open('tester.txt', 'w')
        tempFile.write('')


def main():
    for i in range(0, 50):
        time.sleep(1)
        InsertIntoFile(i)
    # calling Clear function to clear text file
    ClearFile()


if __name__ == '__main__':
    main()
