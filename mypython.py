#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mathew McDade
# CS344 Spring 2019
# Project Py

#Import the useful modules.
from string import ascii_lowercase
from random import choice
from random import randint

#Write 3 new files, each containing 10 random lowercase chars followed by a newline, eg "adejfkpeiq\n".
#File contents should be printed to stdout on program execution.
def random_lowercase_letters_x10():
	for i in range(3):
		#using 'with' sytax makes file operations easy.
		with open("mypy"+str(i+1)+".txt", "w+") as ofile:
			#join random chars using list comprehension.
			letters = ''.join(choice(ascii_lowercase) for x in range(10))
			print(letters)
			letters += '\n'
			ofile.write("%s" % letters)


#Print 2 random integers in the range 1-42 inclusive, each on a new line.
#Print the product of the 2 random numbers on a new line.
def random_two_product():
	random_integer_1 = randint(1,42)	#randint is inclusive, strangely enough.
	random_integer_2 = randint(1,42)
	product = random_integer_1 * random_integer_2
	print(random_integer_1)
	print(random_integer_2)
	print(product)

random_lowercase_letters_x10()
random_two_product()
