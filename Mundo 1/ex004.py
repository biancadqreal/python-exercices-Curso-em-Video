termo = input('Digite um valor: ')
print('O termo é alfanumérico?{} '.format(termo.isalnum())) #só p lembrar do .format()
print('O termo é alfabético?', termo.isalpha())
print('O termo está em ascii?', termo.isascii())
print('O termo é um digito?', termo.isdigit())
print('O termo está em letra minúscula?', termo.islower())
print('O termo é decimal?', termo.isdecimal())
print('O termo é um identificador?', termo.isidentifier())
print('O termo é numérico?', termo.isnumeric())
print('O termo é imprimível?', termo.isprintable())
print('O termo é um espaço?', termo.isspace())
print('O termo está em letra maiúscula?', termo.isupper())
print('O termo é capitalizado?', termo.istitle())