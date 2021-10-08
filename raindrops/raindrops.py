check = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
def convert(number):
    result = ''.join([i[1] for i in check if number % i[0] == 0])
    return str(result or number)