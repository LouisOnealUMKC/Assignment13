#Grades
import unittest

def total(values):
    total = 0
    for i in values:
        total += values[i]
    return float(total)

def average(values):
    total = 0
    if len(values) == 0:
        raise ValueError

    for i in values:
        total += values[i]
    return float(total/len(values))

def median(values):

    sorted = values
    sorted.sort()
    if len(sorted) % 2 == 0:
        return sorted[len(sorted)/2]
    else:
        return (sorted[len(sorted)/2] + sorted[(len(sorted)/2) + 1]) / 2