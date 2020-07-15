"""
class name: basestat.py
@author: Akash Mahajan (@thisisakashmahajan)

You allowed to download and install BaseStat module for your project under following conditions:
* You are not allowed to change, copy or retransmit this code or any part of this file without prior permission from authors
* You are not allowed to disasemble this code.
* Do not use this package to carry out any suspecious activity or you might be in trouble.
* Read the DocString of every method in this package only by using help() method. Ex. help(basestat.getMean)
* You are allowed to carry this code with you anywhere.
* Please report any error or any unexpected behaviour of code on my personal PyPi package page

:) I thank you for using this package in your code.
Email me at: akashmahajan025@gmail.com

"""

class basestat:
    def getMean(self, set_of_numbers):
        """
        Returns the arithmetic mean of set of numbers.

        parameters:
        set_of_numbers (dtype: list())
        a collection of numbers.

        returns:
        a single FLOAT value representing the arithmetic mean of set_of_numbers
        """
        if type(set_of_numbers) is not list:
            raise Exception('Runtime error: set_of_numbers is of type ' + str(type(set_of_numbers)) + '. List expected.')
        return sum(set_of_numbers) / len(set_of_numbers)

    def getIntMean(self, set_of_numbers):
        """
        Returns the integer arithmetic mean of set of numbers.

        parameters:
        set_of_numbers (dtype: list())
        A collection of numbers.

        returns:
        A single INT value representing the integer arithmetic mean of set_of_numbers.
        """
        if type(set_of_numbers) is not list:
            raise Exception('Runtime error: set_of_numbers is of type ' + str(type(set_of_numbers)) + '. List expected.')
        return int(sum(set_of_numbers) / len(set_of_numbers))

    def getMedian(self, set_of_numbers):
        """
        Returns a median of a set of numbers

        parameters:
        set_of_numbers (dtype: list())
        A collection of numbers.

        returns:
        A single INT or FLOAT value representing the median of set_of_numbers.
        """
        if type(set_of_numbers) is not list:
            raise Exception('Runtime error: set_of_numbers is of type ' + str(type(set_of_numbers)) + '. List expected.')
        median = 0
        set_of_numbers = sorted(set_of_numbers)
        if len(set_of_numbers) % 2 == 0:
            first_middle_index = len(set_of_numbers) // 2
            second_middle_index = first_middle_index - 1
            median = (set_of_numbers[first_middle_index] + set_of_numbers[second_middle_index]) / 2
        else:
            middle_index = len(set_of_numbers) // 2
            median = set_of_numbers[middle_index]
        return median

    def getMode(self, set_of_numbers):
        """
        Returns a mode of a set of numbers

        parameters:
        set_of_numbers (dtype: list())
        A collection of numbers.

        returns:
        A single INT or FLOAT representing the mode of set_of_numbers.
        If there is no any mode, returns 1
        """
        if type(set_of_numbers) is not list:
            raise Exception('Runtime error: set_of_numbers is of type ' + str(type(set_of_numbers)) + '. List expected.')
        mode = 0
        set_of_numbers = sorted(set_of_numbers, reverse = True)
        occ_count = 0
        similar_flag = False
        for each_item in set(set_of_numbers):
            ct = set_of_numbers.count(each_item)
            if ct > occ_count:
                occ_count = ct
                mode = each_item
                continue
            if ct == occ_count:
                mode = 1
                break
        return mode
