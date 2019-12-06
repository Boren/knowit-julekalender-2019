import cv2
import numpy

def main():
    im = cv2.imread("mush.png")
    #im = numpy.array([[[240, 33, 11], [61, 78, 109], [69, 46, 106], [104, 45, 160], [36, 192, 143]]])

    prev = None

    for i in range(0, len(im)):
        for j in range(0, len(im[i])):
            if prev is None:
                prev = im[i][j]
                continue

            curr = numpy.copy(im[i][j])

            new = []
            for x in range(3):
                new.append(curr[x]^prev[x])

            im[i][j] = new
            prev = numpy.copy(curr)

    cv2.imwrite('unmush.png', im)

if __name__ == "__main__":
    main()
