import random
import csv

def read_file(filename):
    """Reads a file and returns a list of lines."""
    result = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                concatenated = str(row[0]) + str(row[1])
                result.append(concatenated)
    return result[1:]
def wheel_of_fortune(l):
    """Selects a random candidate from the list."""
    if not l:
        return None
    return random.choice(l)

candidates = read_file('participants.csv')

print(wheel_of_fortune(candidates))