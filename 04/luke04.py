import csv
import numpy
import matplotlib.pylab as plt

kart = numpy.zeros((1000, 1000), dtype="uint64")
total = 0
x = 0
y = 0

with open("coords.csv") as csvfile:
    coordsreader = csv.reader(csvfile, delimiter=",")
    next(coordsreader)

    for coord in coordsreader:
        coordx = int(coord[0])
        coordy = int(coord[1])

        signx = 1 if coordx >= x else -1
        signy = 1 if coordy >= y else -1

        kart[x:coordx:signx, y] += 1
        total += numpy.sum(kart[x:coordx:signx, y])
        x = coordx

        kart[x, y:coordy:signy] += 1
        total += numpy.sum(kart[x, y:coordy:signy])
        y = coordy

print(total)
plt.imshow(kart, cmap="hot", interpolation="nearest")
plt.show()
