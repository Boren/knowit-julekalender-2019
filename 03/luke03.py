import numpy
import math
import scipy.misc

def lagre_bilde(data: str, høyde: int, bredde: int, sti: str):
    bilde = numpy.array(list(data), dtype=int).reshape((høyde, bredde))
    scipy.misc.toimage(bilde, cmin=0.0, cmax=1.0).save(sti)

def main():
    BILDEFIL = 'img.txt'

    with open(BILDEFIL) as f:
        data = f.read()

    lengde = len(data)

    # Finner gyldige høyde x bredde
    oppløsninger = []

    for i in range(2,math.ceil(math.sqrt(lengde))):
        if lengde % i == 0:
            oppløsninger.append((i, lengde//i))
            oppløsninger.append((lengde//i, i))

    # Lagrer alle bildene
    for oppløsning in oppløsninger:
        lagre_bilde(data,
                    oppløsning[0],
                    oppløsning[1],
                    f"./bilder/{oppløsning[0]}x{oppløsning[1]}.png")

if __name__ == "__main__":
    main()