import csv
import sys

sys.setrecursionlimit(100000000)

from LinkedList import LinkedList
from LinkedList import LinkedListEmpty
from LinkedList import LinkedListPopulated

def read():
    result = LinkedListEmpty()

    with open(sys.argv[1]) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            result = result.addFirst(row[0])
    return result
