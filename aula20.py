pri = input('Digite um valor: ')
seg = input('Digite outro valor: ')

if pri > seg : 
    print(f'O primeiro valor ({pri}) é maior do que o segundo valor ({seg})!')
elif seg > pri :
    print(f'O segundo valor ({seg}) é maior do que o primeiro valor ({pri})!')   
else: 
    print('Os valores são iguais!')