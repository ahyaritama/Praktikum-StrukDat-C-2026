from kurs import currency

# Konversi dari mata uang lain ke IDR
def to_idr(curr_from, value):
    return value * currency[curr_from]

# Konversi dari IDR ke mata uang lain
def from_idr(curr_to, value):
    return value / currency[curr_to]

# Konversi mata uang
def convert(curr_from, curr_to, value):
    result = 0
    if curr_from == "IDR" or curr_to == "IDR":
        result = from_idr(curr_to, value) if curr_from == "IDR" else to_idr(curr_from, value)
    else:
        result = from_idr(curr_to, to_idr(curr_from, value))
    return result