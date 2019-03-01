#!/usr/bin/env python
##:: 2019-02-21
##:: Author: Tomas Andriekus
##:: Description: Python from text to:
##:: Text to Binary and Hexadecimal converter
# - *- coding: utf- 8 - *-

from sys import exit
import textwrap

def hex_to_binary(first, second): # Hexadecimal skaiciai nusako 16'liktaine sistema.
	binary = {
	"0": "0000", "1": "0001", "2": "0010", "3": "0011",	"4": "0100", "5": "0101",
	"6": "0110", "7": "0111", "8": "1000", "9": "1001", "10": "1010", "11": "1011",
	"12": "1100", "13": "1101", "14": "1110", "15": "1111"
	}
	x = binary[first]
	y = binary[second]
	z = "%s%s" % (x, y)
	return z

def text_to_table(input): # Is viso yra 256 simboliai lenteleje. Pvz: 32 - reprezentuoja tarpa.
						# +32 Skaicius simbolizuotu mazasias raides. Pvz., 65+32=97 a mazoji. 
	text = {
	"A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72,
	"I": 73, "J": 74, "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80,
	"Q": 81, "R": 82, "S": 83, "T": 84, "U": 85, "V": 86, "W": 87, "X": 88,
	"Y": 89, "Z": 90 
	}
	return text[input]

def table_to_number(input): # Paverskime is table lentos skaiciu i hex / 16 ir prideje liekana:
	first_number = int(input) / 16
	float_number = float(int(input)) / 16
	whats_left = str(float_number-int(float_number))[1:]
	add_second_num = int(0) + float(whats_left) * 16
	regular_number = int(add_second_num)
	return (first_number, regular_number)

def number_to_hex(first, second):
	if second >= 10:
		hex_table = {
		10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
		}
		assign_letter = hex_table[second]
		z = str("%s%s" % (first, assign_letter))
		return z
	else:
		z = int("%i%i" % (first, second))
		return z

def split_text(result):
 	answer = textwrap.wrap(result, 1)
 	return answer

print "Sveiki, tai Text-Hex-Binary konverteris parasytas pagal tomand"
print "Prasau ivesti teksta, kuri noresite isversti i binary: "

# Vartotojas iveda savo texta:
result = raw_input("> ")

# Vartotojo tekstas nusiunciamas i funkcija, kuri isskaido teksta i simbolius
user_answer_to_convert_text = split_text(result)

# For ciklas, kad butu galima paduoti po viena simboli (ji padaryti didziaja raide) ir paduoti
# i funkcija kuri yra python dictionary - sulygins atsakyma su hex skaiciumi:
for i in user_answer_to_convert_text:
	y = i.upper()
	table = text_to_table(y)
	print "\n", y, "-", table, "- This is a number from 256 characters table"
	table_numbers = table_to_number(table)
	hex_result = number_to_hex(table_numbers[0],table_numbers[1])
	print y, "-", "First Hexadecimal number is %i, second Hexadecimal number is: %i" % (table_numbers[0], table_numbers[1])
	print y, "-", hex_result, "- This is a result of %i and %i Hexadecimal values" % (table_numbers[0], table_numbers[1])
	binary_result = hex_to_binary(str(table_numbers[0]), str(table_numbers[1]))
	print y, "-", binary_result, "- This is a result of %s character to binary" % (y)
