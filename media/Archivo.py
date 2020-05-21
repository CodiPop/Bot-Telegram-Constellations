import matplotlib.pyplot as plt

fle = open("../estrellas/stars.txt","r")


cassiopea = {}
cygnet = {}
big_dipper = {}
bootes = {}
gemini = {}
hydra = {}
ursa_major = {}
ursa_minor = {}

casiopea = {}
casiopea_file = open("../estrellas/constelaciones/Casiopea.txt", "r")
Cygnet = {}
Cygnet_file = open("../estrellas/constelaciones/Cygnet.txt", "r")
Boyero = {}
Boyero_file = open("../estrellas/constelaciones/Boyero.txt", "r")
cazo = {}
cazo_file = open("../estrellas/constelaciones/Cazo.txt", "r")
Geminis = {}
Geminis_file = open("../estrellas/constelaciones/Geminis.txt", "r")
Hydra = {}
Hydra_file = open("../estrellas/constelaciones/Hydra.txt", "r")
OsaMayor = {}
OsaMayor_file = open("../estrellas/constelaciones/OsaMayor.txt", "r")
OsaMenor = {}
OsaMenor_file = open("../estrellas/constelaciones/OsaMenor.txt", "r")

def read_coord(file):
    Coordenadas = {}
    Magnitud = {}
    Nombre = {}
    Estrellas = []
    for linea in file:
        Estrellas.append(linea.strip())
    for i in range(len(Estrellas)):
        Estrellas[i] = Estrellas[i].split(' ')
    print(len(Estrellas))
    for star in Estrellas:
        Coordenadas[star[3]] = (star[0], star[1])
        Magnitud[star[3]] = star[4]
        if len(star) >= 7:
            Entra = ''
            for j in range(6, len(star)):
                Entra = Entra + ' ' + star[j]
            ListaAux = Entra.split(';')
            for i in range(len(ListaAux)):
                Nombre[ListaAux[i].strip()] = star[3]
    return (Coordenadas, Magnitud, Nombre)


def read_constellation_lines(file):
    constelaciones = {}
    listaconstelaciones = file.readlines()
    for i in range(len(listaconstelaciones)):
        listaconstelaciones[i] = \
            listaconstelaciones[i].strip().split(',')
    for Estrellas in listaconstelaciones:
        if Estrellas[0] in constelaciones:
            constelaciones[Estrellas[0]].append(Estrellas[1])

        else:
            constelaciones[Estrellas[0]] = [Estrellas[1]]
    return constelaciones


Coordenadas = {}
Magnitudes = {}
NombreEstrellas = {}


Coordenadas, Magnitudes, NombreEstrellas = read_coord(fle)

print(Coordenadas)
