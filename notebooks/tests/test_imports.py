import subprocess
import sys
import textwrap
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[2]
PYIMAGEJ_TIMEOUT_SECONDS = 300


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


# def test_pyimagej_weka_smoke():
#     script = textwrap.dedent(
#         """
#         import os
#         import sys

#         import imagej
#         import numpy as np
#         import scyjava

#         ij = None
#         imp = None
#         result_imp = None
#         weka = None

#         try:
#             # Initialize ImageJ with Fiji (can take minutes to initialize).
#             ij = imagej.init("sc.fiji:fiji")
#             img = ij.io().open("notebooks/illustrations/blobs.gif")

#             # Convert to ImagePlus (Java class) for compatibility with WekaSegmentation.
#             imp = ij.py.to_imageplus(img)

#             WekaSegmentation = scyjava.jimport("trainableSegmentation.WekaSegmentation")
#             weka = WekaSegmentation(imp)

#             classifier_path = "notebooks/illustrations/classifier.model"
#             if not weka.loadClassifier(classifier_path):
#                 raise RuntimeError(f"Could not load classifier: {classifier_path}")

#             # threads=0 means auto threads.
#             result_imp = weka.applyClassifier(imp, 0, False)

#             img_py = ij.py.from_java(result_imp)
#             img_py_n = img_py.to_numpy()

#             assert img_py_n.shape == (3, 254, 256)
#             assert img_py_n.dtype == np.uint8
#             assert img_py_n.min() >= 0
#             assert img_py_n.max() <= 1
#         finally:
#             if weka is not None:
#                 try:
#                     weka.shutDownNow()
#                 except Exception as error:
#                     print(f"Could not stop Weka executor: {error!r}", file=sys.stderr)

#             for image_plus in (result_imp, imp):
#                 if image_plus is not None:
#                     try:
#                         image_plus.close()
#                     except Exception:
#                         pass

#             if ij is not None:
#                 try:
#                     scyjava.jimport("ij.WindowManager").closeAllWindows()
#                 except Exception:
#                     pass

#                 try:
#                     ij.dispose()
#                 except Exception as error:
#                     print(f"Could not dispose ImageJ: {error!r}", file=sys.stderr)

#         sys.stdout.flush()
#         sys.stderr.flush()
#         os._exit(0)
#         """
#     )

#     try:
#         completed = subprocess.run(
#             [sys.executable, "-c", script],
#             cwd=REPO_ROOT,
#             capture_output=True,
#             text=True,
#             timeout=PYIMAGEJ_TIMEOUT_SECONDS,
#         )
#     except subprocess.TimeoutExpired as error:
#         pytest.fail(
#             "PyImageJ/Weka subprocess timed out after "
#             f"{PYIMAGEJ_TIMEOUT_SECONDS} seconds.\n"
#             f"stdout:\n{error.stdout or ''}\n"
#             f"stderr:\n{error.stderr or ''}"
#         )

#     assert completed.returncode == 0, (
#         "PyImageJ/Weka subprocess failed.\n"
#         f"stdout:\n{completed.stdout}\n"
#         f"stderr:\n{completed.stderr}"
#     )
