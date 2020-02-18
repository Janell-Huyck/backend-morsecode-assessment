#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
if sys.version_info[0] >= 3:
    raise Exception("This program requires python2 interpreter")

"""
Morse code decoder

https://www.codewars.com/kata/decode-the-morse-code/python
https://www.codewars.com/kata/decode-the-morse-code-advanced/python


When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
However, the standard does not specify how long that "time unit" is.
And in fact different
operators would transmit at different speed. An amateur person may need a few seconds to
transmit a single character, a skilled professional can transmit 60 words per minute,
and robotic transmitters may go way faster.

OK FOR REAL??  60 WPM??
https://morsecode.scphillips.com/translator.html

For this kata we assume the message receiving is performed automatically by the hardware
that checks the line periodically, and if the line is connected (the key at the remote
station is down), 1 is recorded, and if the line is not connected (remote key is up),
0 is recorded. After the message is fully received, it gets to you for decoding as a
string containing only symbols 0 and 1.
"""

# This dictionary is supplied within the Codewars test suite.
MORSE_CODE = {
    '.-...': '&', '--..--': ',', '....-': '4', '.....': '5', '...---...': 'SOS', '-...': 'B',
    '-..-': 'X', '.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
    '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?', '.----': '1', '-.-': 'K',
    '-..': 'D', '-....': '6', '-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M',
    '-.': 'N', '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
    '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q',
    '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T',
    '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"',
    '-.--.': '(', '---..': '8', '...--': '3'
}


def find_shortest_substring(bits):
    """Return the length of the shortest substring of either 1's or 0's"""

    min_ones = 100000000
    min_zeros = 100000000

    ones_lengths = [len(substring)
                    for substring in bits.split("0") if substring]
    zeros_lengths = [len(substring)
                     for substring in bits.split("1") if substring]

    if ones_lengths:
        min_ones = min(ones_lengths)

    if zeros_lengths:
        min_zeros = min(zeros_lengths)

    return min(min_ones, min_zeros)


def decodeBits(bits):
    """Translate a message string of 1s & 0s to .'s' and -'s"""

    bits = bits.strip("0")
    time_multiplier = find_shortest_substring(bits)

    message = bits[::time_multiplier]

    word_list = message.split("0000000")
    word_list = translate_words(word_list)
    message = message.replace(message, "   ".join(word_list))

    return message


def translate_words(word_list):
    """Translate words of 1's and 0's into a string of .'s and -'s """

    for word in range(0, len(word_list)):
        letter_list = word_list[word].split("000")
        letter_list = translate_letters(letter_list)
        word_list[word] = word_list[word].replace(
            word_list[word], " ".join(letter_list))
    return word_list


def translate_letters(letter_list):
    """Translate letters of 1's and 0's into a string of .'s and -'s"""

    for letter in range(len(letter_list)):
        character_list = letter_list[letter].split("0")
        character_list = translate_characters(character_list)
        letter_list[letter] = letter_list[letter].replace(
            letter_list[letter], "".join(character_list))
    return letter_list


def translate_characters(character_list):
    """Translate short substrings of 1's into .'s and -'s"""

    for char in range(len(character_list)):

        if character_list[char] == "111":
            character_list[char] = character_list[char].replace(
                "111", "-")
        elif character_list[char] == "1":
            character_list[char] = character_list[char].replace(
                "1", ".")
    return character_list


def decodeMorse(morse_code):
    """ Translate a string of dots and dashes into letters """

    result = ""
    morse_code = morse_code.split("   ")

    for word in morse_code:
        letters = word.strip().split(" ")
        word = [list(map(lambda letter:MORSE_CODE.get(letter, ""), letters))]
        word = "".join(word[0])
        word = "".join(word)
        result += word + " "

    return result.strip()
