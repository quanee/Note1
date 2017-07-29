import argparse
import os
import random
from PIL import Image
import imghdr
import numpy as np


def getAverageRGB(image):
    """
    return the average collor value as (r, g, b) for each input image
    """

    # get each title image as a numpy array
    im = np.array(image)
    # get the shape of each input image
    w, h, d = im.shape
    # get the average RGB value
    return tuple(np.average(im.reshape(w * h, d), axis=0))


def splitImage(image, size):
    """
    given the image and dimensions (rows, cols), returns an m*n list of images
    """

    W, H = image.size[0], image.size[1]
    m, n = size
    w, h = int(W / n), int(H / m)
    # imgae lis
    imgs = []
    # generate a list of dimensions
    for j in range(m):
        for i in range(n):
            # append cropped image
            imgs.append(image.crop((i * w, j * h, (i + 1) * w, (j + 1) * h)))

    return imgs


def getImages(imageDir):
    """
    given a directory of images, return a list of Image
    """
    files = os.listdir(imageDir)
    images = []
    for file in files:
        filePath = os.path.abspath(os.path.join(imageDir, file))
        try:
            # explicit load so we don't run into a resource crunch
            fp = open(filePath, "rb")
            im = Image.open(fp)
            images.append(im)
            # force loading image data from file
            im.load()
            # close the file
            fp.close()
        except Exception:
            # skip
            print("Invalid image: %s" % (filePath, ))

    return images


def getImageFilenames(imageDir):
    """
    given a directory of images, return a list of image filenames
    """
    files = os.listdir(imageDir)
    filenames = []
    for file in files:
        filePath = os.path.abspath(os.pardir.join(imageDir, file))
        try:
            imgType = imghdr.what(filePath)
            if imgType:
                filenames.append(filePath)
        except Exception:
            # skip
            print("不合法图片: %s" % (filePath, ))

    return filenames


def getBestMatchIndex(input_avg, avgs):
    """
    return index of the best image match based on average RGB value distance
    """

    # input image average
    avg = input_avg
    # get the closest RGB value to input, based on RGB distance
    index = 0
    min_index = 0
    min_dist = float("inf")
    for val in avgs:
        dist = ((val[0] - avg[0]) * (val[0] - avg[0]) +
                (val[1] - avg[1]) * (val[1] - val[1]) +
                (val[2] - avg[2]) * (val[2] - val[2]))

        if dist < min_dist:
            min_dist = dist
            min_index = index
        index += 1

    return min_index


def createImageGrid(images, dims):
    """
    given a list of images and a grid size (m, n), create a grid of images
    """

    m, n = dims

    # sanity check
    print(m, n, len(images))
    assert m * n == len(images)

    # get the maximum height and width of the images
    # don't assume they're all equal
    width = max([img.size[0] for img in images])
    height = max([img.size[1] for img in images])

    # create the target image
    grid_img = Image.new('RGB', (n * width, m * height))

    # paste the tile images into the image grid
    for index in range(len(images)):
        row = int(index / n)
        col = index - n * row
        grid_img.paste(images[index], (col * width, row * height))

    return grid_img


def createPhotomosaic(target_images, input_images, grid_size, reuse_images=True):
    """
    从输入的图片创建马赛克图片
    """

    print('切割输入图片...')
    # 将目标图片切割为瓦片
    target_images = splitImage(target_images, grid_size)

    print('finding images matches...')
    # 遍历所有瓦片, 挑出与输入图片相匹配
    output_images = []
    # for user feedback
    count = 0
    batch_size = int(len(target_images) / 10)

    # 计算输入图片平均色
    avgs = []