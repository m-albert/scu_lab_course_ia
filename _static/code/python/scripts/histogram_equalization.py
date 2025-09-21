from skimage.io import imread
from skimage.exposure import histogram
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def histogram_equalization(img):
    """Implements histogram equalization.
    
    @param img: Image to be equalized (numpy array)
    
    @return equalized image.
    """

    # Calculate the normalized histogram (sums to 1.0): this is 
    # the probability mass function of the image intensity values.
    p = histogram(img, source_range="dtype", normalize=True)[0]

    # Calculate the cumulative histogram
    t = np.cumsum(p)

    # Equalize the histogram (L = 255 for 8-bit images and 65535 for 16-bit images)
    L = np.iinfo(img.dtype).max
    S = np.round(L * t)

    # Initialize the output image
    img_eq = np.zeros(img.shape, dtype=img.dtype)

    # Now use the equalized histogram to update the image (we use a double for
    # loop to make the process more obvious)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            r = img[y, x]
            img_eq[y, x] = S[r]

    # Return the equalized image
    return img_eq


if __name__ == "__main__":
    
    # Little trick to build the proper path
    p = Path(__file__).parent / "pout.tif"

    # Read the example image 
    img = imread(p)

    # Run histogram equalization
    img_eq = histogram_equalization(img)
    
    # Show original and equalized image
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(img, cmap="gray")
    ax1.set_title("Original image")
    ax2.imshow(img_eq, cmap="gray")
    ax2.set_title("Equalized image")
    plt.suptitle("Close to continue...")
    plt.show()
