def inverter_string(string):
    return string[::-1]
string_original = input("Digite uma palavra: ")


string_invertida = inverter_string(string_original)
print("Palavra invertida:", string_invertida)
