from skimage.io import imread
import matplotlib.pyplot as plt
from pathlib import Path


def iterative_threshold(img, t):
    """Implements iterative thresholding.
    
    @param img: Image to be segmented (numpy array)
    @param t  : Initial threshold (float)
    
    @return Tuple of black-and-white image and final threshold value.
    """

    # Make sure the initial threshold t does not give empty sets
    mx = img.max()
    mn = img.min()

    if t >= mx or t < mn:
        t = (mn + mx) / 2 
        print(f"The initial threshold was outside the dynamic "
              "range of the image and was reset to {t}.")

    # This is the actual algorithm
    tlast = t + 1.0

    while abs(t - tlast) > 0.05:

        # Get the two subsets
        G1 = img[img > t]
        G2 = img[img <= t]

        # Calculate the means
        m1 = G1.mean()
        m2 = G2.mean()
        
        # Calculate the new threshold (but first store last value)
        tlast = t
        t = (m1 + m2) / 2

    # Segment with the calculated threshold
    BW = img > t
    
    # Return black-and-white mask and last value of t
    return BW, t


if __name__ == "__main__":
    
    # Little trick to build the proper path
    p = Path(__file__).parent / "neuron.tif"

    # Read the example image 
    img = imread(p)

    # Our initial t is set to 128; try other values!
    BW, t = iterative_threshold(img, 128)  
    
    # Show image and black-and-white mask
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(img, cmap="gray")
    ax1.set_title("Original image")
    ax2.imshow(BW, cmap="gray")
    ax2.set_title("Black-and-white mask")
    plt.suptitle("Close to continue...")
    plt.show()    
    print(f"The final threshold is t = {t}.")
