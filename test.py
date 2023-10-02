import numpy as np
from PIL import Image


def apply_clut():
    # get the CLUT and the DEM
    clut = get_clut()
    test_dem = get_test_dem()

    # initialize output array
    output = np.zeros(test_dem.shape, dtype=np.uint8)

    # fill output array with clut data
    output[:,:,:] = clut[test_dem[:,:,0],0,:]

    # save as an image
    save_output(output)


def save_output(output):
    clut_image = Image.fromarray(output)
    clut_image.save("output.png")


def get_clut():
    clut_image = Image.open("clut.png")
    return np.asarray(clut_image)


def get_test_dem():
    #dem_image = Image.open("test_dem.png")
    dem_image = Image.open(f"biomes/snow/dem.png")
    return np.asarray(dem_image)


if __name__ == "__main__":
    apply_clut()