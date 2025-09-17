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