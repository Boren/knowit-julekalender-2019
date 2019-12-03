import timeit
import numpy
import scipy.misc
from PIL import Image

def main():
    WORLDFIL = 'world.txt'
    SAVE_IMAGE = False

    vann = 0

    with open(WORLDFIL) as f:
        verden = f.read()
    
    verden = verden.replace(" ", "0")
    verden = verden.replace("#", "1")
    verden = verden.splitlines()
    verden = [list(x) for x in verden]
    verden = numpy.array(verden, dtype=int)

    if SAVE_IMAGE:
        scipy.misc.toimage(verden, cmin=0.0, cmax=1.0).save('./verden.png')

    for radid, rad in enumerate(verden):
        forrigeverdi = rad[0]
        sistbytteindex = 0
        på = False

        for kolonneid, kolonne in enumerate(rad[1:]):
            if forrigeverdi == 1 and kolonne == 0:
                sistbytteindex = kolonneid
                på = True
            elif forrigeverdi == 0 and kolonne == 1 and på:
                vann += kolonneid - sistbytteindex
                på = False
                verden[radid][sistbytteindex+1:kolonneid+1] = 2

            forrigeverdi = kolonne

    if SAVE_IMAGE:
        fargekart = {
            0: [255, 255, 255],
            1: [124, 252, 0],
            2: [0, 119, 190]
        }

        verden_rgb = numpy.zeros((verden.shape[0], verden.shape[1], 3))

        for radid, rad in enumerate(verden):
            for kolonneid, kolonne in enumerate(rad):
                verden_rgb[radid][kolonneid] = fargekart[kolonne]

        Image.fromarray(verden_rgb.astype('uint8'), 'RGB').save('./verdenmedvann.png')

    print(vann)

if __name__ == "__main__":
    elapsed_time = timeit.timeit(main, number=100)/100
    print(elapsed_time)