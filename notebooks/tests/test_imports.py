def test_imports():
    """
    Test that all imports are successful.
    """
    import skimage
    from cellpose import models
    

def test_cellpose():
    """
    Test that
    - cellpose can be imported
    - a model can be instantiated
    - the model can be run on a random image
    """
    from cellpose import models
    import numpy as np

    model = models.Cellpose(gpu=False, model_type='cyto')
    img = np.random.rand(100, 100)
    masks, flows, styles, diams = model.eval(img, diameter=None, channels=[0, 0])
    assert masks.shape == img.shape


def test_pyimagej():
    import os
    import imagej
    import scyjava
    import imageio
    import numpy as np
    import matplotlib.pyplot as plt
    from skimage.measure import label
    from skimage.io import imsave, imread
    from iaf.plot import imshow, show_labels
    from iaf.morph.watershed import estimate_object_sizes, separate_neighboring_objects

    # Initialize ImageJ with Fiji (can take minutes to initialize) 
    ij = imagej.init('sc.fiji:fiji')

    img = ij.io().open('../illustrations/blobs.gif')

    # Convert to ImagePlus (Java class) for compatibility with WekaSegmentation
    imp = ij.py.to_imageplus(img)

    # Create WekaSegmentation object with the image
    WekaSegmentation = scyjava.jimport('trainableSegmentation.WekaSegmentation')
    weka = WekaSegmentation(imp)

    # Load pre-trained classifier model (change to your .model file path)
    classifier_path = r'../illustrations/classifier.model'
    weka.loadClassifier(classifier_path)

    # Apply the classifier to image, arguments: (ImagePlus, threads=0 auto, getProbabilities=False)
    result_imp = weka.applyClassifier(imp, 0, False)

    img_py = ij.py.from_java(result_imp)
    img_py_n = img_py.to_numpy()
