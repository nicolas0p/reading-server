
## Writes a number containing one digit in full
# @param number number to be written in full
# @param digit_reading list of readings of single digits
# @return string containing the reading in full of the number
def handle_ones(number, digit_reading):
    if number == 0:
        return ""
    return digit_reading[number - 1]

## Writes a number containing two digits in full
# @param number number to be written in full
# @param digit_reading list of readings of single digits
# @param tens_reading list of readings for multiples of ten
# @param irregulars_reading dict of {irregular_number : its reading}
# @param filler word that goes between number readings
# @return string containing the reading in full of the number
def handle_tens_and_ones(number, digit_reading, tens_reading, irregulars_reading, filler):
    if number in irregulars_reading:
        return irregulars_reading[number]
    ones_digit = int(str(number)[-1])
    ones = handle_ones(ones_digit, digit_reading)
    tens_ones = ones
    if len(str(number)) >= 2 and int(str(number)[-2]) != 0:
        tens_digit = int(str(number)[-2])
        tens = tens_reading[tens_digit - 1]
        if ones_digit == 0:
            tens_ones = tens
        else:
            tens_ones = tens + filler + ones
    return tens_ones


## Writes a number in full in Portuguese.
# @param number in [-99999, 99999] integer to be read.
# @return string containing the given number written in full in Portuguese.
def portuguese_number_reader(number):
    digit_reading = [
            "um",
            "dois",
            "três",
            "quatro",
            "cinco",
            "seis",
            "sete",
            "oito",
            "nove",
            ]
    tens_reading = [
            "dez",
            "vinte",
            "trinta",
            "quarenta",
            "cinquenta",
            "sessenta",
            "setenta",
            "oitenta",
            "noventa",
            ]
    irregulars_reading = {
            0: "zero",
            11: "onze",
            12: "doze",
            13: "treze",
            14: "quatorze",
            15: "quinze",
            16: "dezesseis",
            17: "dezessete",
            18: "dezoito",
            19: "dezenove",
            100: "cem",
            }
    hundreds_reading = [
            "cento",
            "duzentos",
            "trezentos",
            "quatrocentos",
            "quinhentos",
            "seiscentos",
            "setecentos",
            "oitocentos",
            "novecentos",
            ]
    filler = ' e '
    thousand_marker = 'mil'
    signal = ""
    if number < 0:
        signal = "menos "
        number = -number
    if number in irregulars_reading:
        return irregulars_reading[number]
    #only need to write zero when it is on its own
    del irregulars_reading[0]

    tens_ones_number = int(str(number)[-2:])
    tens_ones = handle_tens_and_ones(tens_ones_number, digit_reading,
            tens_reading, irregulars_reading, filler)

    hundreds = ""
    if len(str(number)) >= 3 and int(str(number)[-3]) != 0:
        hundreds_digit = int(str(number)[-3])
        hundreds = hundreds_reading[hundreds_digit - 1]
        #handle irregularities
        complete_hundred = int(str(number)[-3:])
        if complete_hundred in irregulars_reading:
            hundreds = irregulars_reading[complete_hundred]
        if tens_ones != "":
            hundreds += filler

    thousands = ""
    if len(str(number)) >= 4:
        tens_one_thousands_number = int(str(number)[-5:-3])
        tens_one_thousands = handle_tens_and_ones(tens_one_thousands_number,
                digit_reading, tens_reading, irregulars_reading, filler)
        if tens_one_thousands != "":
            thousands = tens_one_thousands + " " + thousand_marker
            if tens_one_thousands_number == 1:
                thousands = thousand_marker
            hundreds_digit = int(str(number)[-3]) #it may have not been defined
            if hundreds_digit * 100 + tens_ones_number != 0:
                thousands += filler
    return signal + thousands + hundreds + tens_ones
