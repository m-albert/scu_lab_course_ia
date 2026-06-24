def test_pyimagej_full():
    import imagej
    import numpy as np
    import scyjava

    # Initialize ImageJ with Fiji (can take minutes to initialize).
    ij = imagej.init("sc.fiji:fiji")

    img = ij.io().open("notebooks/illustrations/blobs.gif")

    # Convert to ImagePlus (Java class) for compatibility with WekaSegmentation.
    imp = ij.py.to_imageplus(img)

    WekaSegmentation = scyjava.jimport("trainableSegmentation.WekaSegmentation")
    weka = WekaSegmentation(imp)

    classifier_path = "notebooks/illustrations/classifier.model"
    assert weka.loadClassifier(classifier_path)

    # Apply the classifier to image, arguments: (ImagePlus, threads=0 auto, getProbabilities=False).
    result_imp = weka.applyClassifier(imp, 0, False)

    img_py = ij.py.from_java(result_imp)
    img_py_n = img_py.to_numpy()

    assert img_py_n.shape == (3, 254, 256)
    assert img_py_n.dtype == np.uint8
