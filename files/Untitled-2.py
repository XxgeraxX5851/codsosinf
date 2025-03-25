with open('alumnos.txt', 'r')as fichero:
    for line in fichero.readlines():
        print(line,end='')


lista = ['angeles Hernandez Alan dwii\n ',
'Sandoval Camacho Joel Alejandro\n ',
'torres Jimenez  Job Esau\n' ,
'robles gomez Efren alexander\n' ,
'Montaño Hernandez Yamilet isabela\n ',
'Bayardo  Fregoso Carlos Eduardo\n ',
'garcia herrera david iyari\n',
'sanches Ortiz Lizbeth estefania\n ',
'perez hernandez sophia yuriko\n' ,
'parra almado Emmanuel alejandro\n']
with open('alumnos.txt', 'w')as fichero:
    fichero.writelines(lista)

with open('alumnos.txt', 'r')as fichero:
    for line in fichero.readlines():
        print(line,end='')