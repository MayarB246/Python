letra_a = 'A'
letra_b = 'B'
letra_c = 1.1

string = 'b={b} a={a} b={b} c={c:.2f}    ddd=   {s}'
formato = string.format(a=letra_a, b=letra_b, c=letra_c, s=string)

print(formato)