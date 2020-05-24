import matplotlib.pyplot as plt
import numpy as np

fle = open("../estrellas/stars.txt","r")


plt.style.use('dark_background')
plt.figure(
    figsize=(18, 12))

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



def Firmamento(file):
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


def Constelaciones(file):
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


def graficarEstrellas(coordenadas,Constelaciones,NombreEstrellas):
    plt.axis('off')
    x = []
    y = []
    for star in coordenadas:
        # position turtle at the x and y coordinate for the star
        x.append(float(coordenadas[star][0]))
        y.append(float(coordenadas[star][1]))
    print(x)

    for Constelacion in Constelaciones:
        xstart = []
        ystart = []
        xend = []
        yend = []
        for star in Constelacion:
            for point_to_star in Constelacion[star]:
                Aux = NombreEstrellas[star]
                start_x = float(coordenadas[Aux][0])
                start_y = float(coordenadas[Aux][1])
                xstart.append(start_x)
                ystart.append(start_y)
                Aux = NombreEstrellas[point_to_star]
                end_x = float(coordenadas[Aux][0])
                end_y = float(coordenadas[Aux][1])
                xend.append(end_x)
                yend.append(end_y)
        rgb = np.random.rand(3,)
        plt.plot(xstart,ystart,xend,yend,color=rgb ,marker ="o")

def GraficarCasiopea(coordenadas,Constelacion,NombreEstrellas):
    plt.figure(
        figsize=(18, 12))
    PlotStars(coordenadas)
    plt.axis('off')
    x = []
    y = []
    for star in coordenadas:
        # position turtle at the x and y coordinate for the star
        x.append(float(coordenadas[star][0]))
        y.append(float(coordenadas[star][1]))
    print(x)
    xstart = []
    ystart = []
    xend = []
    yend = []
    for star in Constelacion:
        for point_to_star in Constelacion[star]:
            Aux = NombreEstrellas[star]
            start_x = float(coordenadas[Aux][0])
            start_y = float(coordenadas[Aux][1])
            xstart.append(start_x)
            ystart.append(start_y)
            Aux = NombreEstrellas[point_to_star]
            end_x = float(coordenadas[Aux][0])
            end_y = float(coordenadas[Aux][1])
            xend.append(end_x)
            yend.append(end_y)
    rgb = np.random.rand(3,)
    plt.plot(xstart,ystart,xend,yend,color=rgb ,marker ="o")
    plt.savefig('../media/casiopea.jpg', dpi=500, bbox_inches='tight')
    plt.show()

def GraficarCygnet(coordenadas,Constelacion,NombreEstrellas):
    plt.figure(
        figsize=(18, 12))
    PlotStars(coordenadas)
    plt.axis('off')
    x = []
    y = []
    for star in coordenadas:
        # position turtle at the x and y coordinate for the star
        x.append(float(coordenadas[star][0]))
        y.append(float(coordenadas[star][1]))
    print(x)
    xstart = []
    ystart = []
    xend = []
    yend = []
    for star in Constelacion:
        for point_to_star in Constelacion[star]:
            Aux = NombreEstrellas[star]
            start_x = float(coordenadas[Aux][0])
            start_y = float(coordenadas[Aux][1])
            xstart.append(start_x)
            ystart.append(start_y)
            Aux = NombreEstrellas[point_to_star]
            end_x = float(coordenadas[Aux][0])
            end_y = float(coordenadas[Aux][1])
            xend.append(end_x)
            yend.append(end_y)
    rgb = np.random.rand(3,)
    plt.plot(xstart,ystart,xend,yend,color=rgb ,marker ="o")
    plt.savefig('../media/Cygnet.jpg', dpi=500, bbox_inches='tight')
    plt.show()

def GraficarBoyero(coordenadas,Constelacion,NombreEstrellas):
    plt.figure(
        figsize=(18, 12))
    PlotStars(coordenadas)
    plt.axis('off')
    x = []
    y = []
    for star in coordenadas:
        # position turtle at the x and y coordinate for the star
        x.append(float(coordenadas[star][0]))
        y.append(float(coordenadas[star][1]))
    print(x)
    xstart = []
    ystart = []
    xend = []
    yend = []
    for star in Constelacion:
        for point_to_star in Constelacion[star]:
            Aux = NombreEstrellas[star]
            start_x = float(coordenadas[Aux][0])
            start_y = float(coordenadas[Aux][1])
            xstart.append(start_x)
            ystart.append(start_y)
            Aux = NombreEstrellas[point_to_star]
            end_x = float(coordenadas[Aux][0])
            end_y = float(coordenadas[Aux][1])
            xend.append(end_x)
            yend.append(end_y)
    rgb = np.random.rand(3,)
    plt.plot(xstart,ystart,xend,yend,color=rgb ,marker ="o")
    plt.savefig('../media/Boyero.jpg', dpi=500, bbox_inches='tight')
    plt.show()

def Graficarcazo(coordenadas,Constelacion,NombreEstrellas):
    plt.figure(
        figsize=(18, 12))
    PlotStars(coordenadas)
    plt.axis('off')
    x = []
    y = []
    for star in coordenadas:
        # position turtle at the x and y coordinate for the star
        x.append(float(coordenadas[star][0]))
        y.append(float(coordenadas[star][1]))
    print(x)
    xstart = []
    ystart = []
    xend = []
    yend = []
    for star in Constelacion:
        for point_to_star in Constelacion[star]:
            Aux = NombreEstrellas[star]
            start_x = float(coordenadas[Aux][0])
            start_y = float(coordenadas[Aux][1])
            xstart.append(start_x)
            ystart.append(start_y)
            Aux = NombreEstrellas[point_to_star]
            end_x = float(coordenadas[Aux][0])
            end_y = float(coordenadas[Aux][1])
            xend.append(end_x)
            yend.append(end_y)
    rgb = np.random.rand(3,)
    plt.plot(xstart,ystart,xend,yend,color=rgb ,marker ="o")
    plt.savefig('../media/cazo.jpg', dpi=500, bbox_inches='tight')
    plt.show()

def GraficarGeminis(coordenadas,Constelacion,NombreEstrellas):
    plt.figure(
        figsize=(18, 12))
    PlotStars(coordenadas)
    plt.axis('off')
    x = []
    y = []
    for star in coordenadas:
        # position turtle at the x and y coordinate for the star
        x.append(float(coordenadas[star][0]))
        y.append(float(coordenadas[star][1]))
    print(x)
    xstart = []
    ystart = []
    xend = []
    yend = []
    for star in Constelacion:
        for point_to_star in Constelacion[star]:
            Aux = NombreEstrellas[star]
            start_x = float(coordenadas[Aux][0])
            start_y = float(coordenadas[Aux][1])
            xstart.append(start_x)
            ystart.append(start_y)
            Aux = NombreEstrellas[point_to_star]
            end_x = float(coordenadas[Aux][0])
            end_y = float(coordenadas[Aux][1])
            xend.append(end_x)
            yend.append(end_y)
    rgb = np.random.rand(3,)
    plt.plot(xstart,ystart,xend,yend,color=rgb ,marker ="o")
    plt.savefig('../media/Geminis.jpg', dpi=500, bbox_inches='tight')
    plt.show()

def GraficarHydra(coordenadas,Constelacion,NombreEstrellas):
    plt.figure(
        figsize=(18, 12))
    PlotStars(coordenadas)
    plt.axis('off')
    x = []
    y = []
    for star in coordenadas:
        # position turtle at the x and y coordinate for the star
        x.append(float(coordenadas[star][0]))
        y.append(float(coordenadas[star][1]))
    print(x)
    xstart = []
    ystart = []
    xend = []
    yend = []
    for star in Constelacion:
        for point_to_star in Constelacion[star]:
            Aux = NombreEstrellas[star]
            start_x = float(coordenadas[Aux][0])
            start_y = float(coordenadas[Aux][1])
            xstart.append(start_x)
            ystart.append(start_y)
            Aux = NombreEstrellas[point_to_star]
            end_x = float(coordenadas[Aux][0])
            end_y = float(coordenadas[Aux][1])
            xend.append(end_x)
            yend.append(end_y)
    rgb = np.random.rand(3,)
    plt.plot(xstart,ystart,xend,yend,color=rgb ,marker ="o")
    plt.savefig('../media/Hydra.jpg', dpi=500, bbox_inches='tight')
    plt.show()

def GraficarOsaMenor(coordenadas,Constelacion,NombreEstrellas):
    plt.figure(
        figsize=(18, 12))
    PlotStars(coordenadas)
    plt.axis('off')
    x = []
    y = []
    for star in coordenadas:
        # position turtle at the x and y coordinate for the star
        x.append(float(coordenadas[star][0]))
        y.append(float(coordenadas[star][1]))
    print(x)
    xstart = []
    ystart = []
    xend = []
    yend = []
    for star in Constelacion:
        for point_to_star in Constelacion[star]:
            Aux = NombreEstrellas[star]
            start_x = float(coordenadas[Aux][0])
            start_y = float(coordenadas[Aux][1])
            xstart.append(start_x)
            ystart.append(start_y)
            Aux = NombreEstrellas[point_to_star]
            end_x = float(coordenadas[Aux][0])
            end_y = float(coordenadas[Aux][1])
            xend.append(end_x)
            yend.append(end_y)
    rgb = np.random.rand(3,)
    plt.plot(xstart,ystart,xend,yend,color=rgb ,marker ="o")
    plt.savefig('../media/OsaMenor.jpg', dpi=500, bbox_inches='tight')
    plt.show()

def GraficarOsaMayor(coordenadas,Constelacion,NombreEstrellas):
    plt.figure(
        figsize=(18, 12))
    PlotStars(coordenadas)
    plt.axis('off')
    x = []
    y = []
    for star in coordenadas:
        # position turtle at the x and y coordinate for the star
        x.append(float(coordenadas[star][0]))
        y.append(float(coordenadas[star][1]))
    print(x)
    xstart = []
    ystart = []
    xend = []
    yend = []
    for star in Constelacion:
        for point_to_star in Constelacion[star]:
            Aux = NombreEstrellas[star]
            start_x = float(coordenadas[Aux][0])
            start_y = float(coordenadas[Aux][1])
            xstart.append(start_x)
            ystart.append(start_y)
            Aux = NombreEstrellas[point_to_star]
            end_x = float(coordenadas[Aux][0])
            end_y = float(coordenadas[Aux][1])
            xend.append(end_x)
            yend.append(end_y)
    rgb = np.random.rand(3,)
    plt.plot(xstart,ystart,xend,yend,color=rgb ,marker ="o")
    plt.savefig('../media/OsaMayor.jpg', dpi=500, bbox_inches='tight')
    plt.show()




def plot_plain_stars(coordenadas):
    PlotStars(coordenadas)
    cont = 0
    x = []
    y = []
    for star in coordenadas:
        # position turtle at the x and y coordinate for the star
        x.append(float(coordenadas[star][0]))
        y.append(float(coordenadas[star][1]))
        cont+=1
    print(x)
    plt.scatter(x,y,c="w")
    plt.axis([-1,1,-1,1])
    plt.savefig('../media/Todaslasimage.jpg', dpi=500, bbox_inches='tight')
    plt.show()


def PlotStars(coordenadas):
    cont = 0
    x = []
    y = []
    for star in coordenadas:
        # position turtle at the x and y coordinate for the star
        x.append(float(coordenadas[star][0]))
        y.append(float(coordenadas[star][1]))
        cont += 1
    print(x)
    plt.scatter(x, y, c="w")


Coordenadas = {}
Magnitudes = {}
NombreEstrellas = {}


Coordenadas, Magnitudes, NombreEstrellas = Firmamento(fle)


casiopea = Constelaciones(casiopea_file)
Cygnet = Constelaciones(Cygnet_file)
Boyero = Constelaciones(Boyero_file)
cazo = Constelaciones(cazo_file)
Geminis = Constelaciones(Geminis_file)
Hydra = Constelaciones(Hydra_file)
OsaMayor = Constelaciones(OsaMayor_file)
OsaMenor = Constelaciones(OsaMenor_file)

misConstelaciones = [casiopea,Cygnet,Boyero,cazo,Geminis,Hydra,OsaMayor,OsaMenor]

graficarEstrellas(Coordenadas,misConstelaciones,NombreEstrellas)
plot_plain_stars(Coordenadas)
GraficarCasiopea(Coordenadas,casiopea,NombreEstrellas)
GraficarCygnet(Coordenadas,Cygnet,NombreEstrellas)
GraficarBoyero(Coordenadas,Boyero,NombreEstrellas)
Graficarcazo(Coordenadas,cazo,NombreEstrellas)
GraficarGeminis(Coordenadas,Geminis,NombreEstrellas)
GraficarHydra(Coordenadas,Hydra,NombreEstrellas)
GraficarOsaMayor(Coordenadas,OsaMayor,NombreEstrellas)
GraficarOsaMenor(Coordenadas,OsaMenor,NombreEstrellas)






