========
GiftCard
========

============
Introduction
============

Scripts to find the items to purchase with a certain gift card balance.

=========
Objective
=========

The objective of find_price.py is to find 2 gifts from a file of items such that
the sum of the prices are closest to but within the balance in the gift card.

The objective of bonus.py is to find 3 gifts from a file of items, again under
the same constraints.

Assumptions:

    - The prices are in sorted order
    - There are no duplicates, each item is unique
    - Only one solution is needed even though multiple may exist

=====================
Logic and Performance
=====================

The approach to solve both find_price.py and bonus.py is by storing
all sorted items in the file into an array . Two pointers
left, right move in from both ends of the array to find the two items
with the most optimal sum which is called target.

find_price.py:

left and right both are initially assigned to each end of the array, left
containing the smallest and right containing the largest value.

If their sum is bigger than target, the right pointer moves left, reducing
in value.

If their sum is smaller than target, the left pointer moves right, increasing in value.

closest_l, closest_r are pointers that store the items that have the closest sum lesser
than the target value encountered so far.

If the sum adds up to target value, the two items are printed.

If all items are spanned (i.e left and right have reached the same element), the closest
items encountered so far is printed.

If no items are encountered with value lower than the target amount, "Not possible" is printed.

Since each item in the array is scanned just once for comparison, the time complexity is O(n) where
n is the number of items.
Since we use an array to store all the items in the file, the space complexity is O(n).

bonus.py:

The approach of two pointers is used to find the pair of items to find an optimal sum for
each element in the array.

For each element of the array , elements after it are scanned to find a pair such that
the sum of them element's price and the pair's is closest to the sum.

closest_k, closest_l, closest_r are still used to track the items whose sum was closest
to the target amongst items scanned so far.

Since scanning of the array is done for each element the time complexity is O(n^2).
The space complexity is still O(n). No extra storage space is required.


=============
Running Tests
=============

The test suite can be run against a single Python version which requires ```pip install pytest``` and optionally ```pip install pytest-cov``` (these are included if you have installed dependencies from ```requirements.testing.txt```)

To run the unit tests with a single Python version::

    $ py.test -v

to also run code coverage::

    $ py.test -v --cov-report xml --cov=find_price

------------
Sample Usage
------------

.. code::

    $python find_price.py prices.txt 2500
    Candy Bar 500, Earmuffs 2000

    $python find_price.py prices.txt 1100
    Not possible

    $python bonus.py prices.txt 100000
    Headphones 1400, Earmuffs 2000, Bluetooth Stereo 6000

    $python bonus.py prices.txt 100
    Not possible

