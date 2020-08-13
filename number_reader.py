
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
    filler = ' e '
    digit = digit_reading[int(str(number)[-1])]
    if len(str(number)) == 1:
        return digit
    if len(str(number)) == 2:

        ten = tens_reading[int(str(number)[0]) - 1]
        if int(str(number)[1]) == 0:
            return ten

        return ten + filler + digit
