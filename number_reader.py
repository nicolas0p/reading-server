
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
    filler = ' e '
    ones_digit = int(str(number)[-1])
    ones_reading = digit_reading[ones_digit]
    if len(str(number)) == 1:
        return ones_reading
    if len(str(number)) == 2:

        tens_digit = int(str(number)[0])
        tens = tens_reading[tens_digit - 1]
        if int(str(number)[1]) == 0:
            return tens

        if tens_digit == 1:
            return irregular_tens_reading[ones_digit - 1]

        return tens + filler + ones_reading
