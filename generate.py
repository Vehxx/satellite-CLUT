import numpy as np
from PIL import Image


def generate_clut():
    # initialize array and fill with background color
    clut = np.zeros([256, 1, 4], dtype=np.uint8)
    clut[:,:,0].fill(255)
    clut[:,:,3].fill(255)

    # get color and height information
    sample_color = get_biome_color("snow")
    sample_height = get_biome_dem("snow")

    clut[sample_height[:,:,0],0,:] = sample_color[:,:,:]

    # save as an image
    save_clut(clut)


def save_clut(clut):
    clut_image = Image.fromarray(clut)
    clut_image.save("clut.png")


def get_biome_color(biome):
    color_image = Image.open(f"biomes/{biome}/color.png")
    return np.asarray(color_image)


def get_biome_dem(biome):
    dem_image = Image.open(f"biomes/{biome}/dem.png")
    return np.asarray(dem_image)


if __name__ == "__main__":
    generate_clut()