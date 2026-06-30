import mrcfile
import numpy as np
from skimage.util import montage
from skimage.transform import resize
import matplotlib.pyplot as plt
import math

def make_montage_mrcs(fn):
    with mrcfile.open(fn) as mrc:
        stack = mrc.data
        nz = stack.shape[0]
        w = math.ceil(math.sqrt(nz)*4/3)
        h = math.ceil(nz/w)
        norm = (stack-np.min(stack,axis=(1,2),keepdims=True))/(np.max(stack,axis=(1,2),keepdims=True)-np.min(stack,axis=(1,2),keepdims=True))
        arr_out = montage(norm, padding_width=2, fill=0, grid_shape=(h,w))

        plt.imshow(arr_out, cmap="gray")
        fn_out = fn.replace(".mrc", ".webp")
        plt.savefig(fn_out, format="webp", bbox_inches="tight")
        # print(mrc.data.shape)


def convert_mrc(fn):
    with mrcfile.open(fn) as mrc :
        img = mrc.data
        print("Before :", img.shape)
        img_resized = resize(img, (img.shape[0]//4, img.shape[1]//4), anti_aliasing=True)
        print("After :", img_resized.shape)

        norm = (img-np.min(img))/(np.max(img)-np.min(img))

        fn_out = fn.replace(".mrc", ".webp")
        print(fn_out)
        plt.imshow(img_resized, cmap="gray")
        plt.axis('off')
        plt.savefig(fn_out, format="webp", bbox_inches="tight")
        plt.show()

convert_mrc("mx2441_grid5_12134.mrc")