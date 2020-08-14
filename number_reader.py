
## Writes a number in full in Portuguese.
# @param number in [-99999, 99999] integer to be read.
# @return string containing the given number written in full in Portuguese.
def portuguese_number_reader(number):
    digit_reading = [
            "zero",
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
    irregular_tens_reading = [
            "onze",
            "doze",
            "treze",
            "quatorze",
            "quinze",
            "dezesseis",
            "dezessete",
            "dezoito",
            "dezenove",
            ]
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
    ones_digit = int(str(number)[-1])
    ones = digit_reading[ones_digit]
    tens_ones = ""
    hundreds = ""
    tens_ones = ones
    if len(str(number)) >= 2 and int(str(number)[-2]) != 0:
        tens_digit = int(str(number)[-2])
        tens = tens_reading[tens_digit - 1]
        if ones_digit == 0:
            tens_ones = tens
        else:
            tens_ones = tens + filler + ones
            if tens_digit == 1:
                tens_ones = irregular_tens_reading[ones_digit - 1]

    if len(str(number)) >= 3:
        hundreds_digit = int(str(number)[-3])
        hundreds = hundreds_reading[hundreds_digit - 1]
        if tens_ones == "zero":
            tens_ones = ""
            if hundreds_digit == 1:
                hundreds = "cem"
        else:
            hundreds += filler
    return hundreds + tens_ones
