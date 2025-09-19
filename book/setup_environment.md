# Setting up a python environment

Running the notebooks in this course requires a python environment with the necessary packages installed. This section explains how to set up the right environment using `conda` and the `environment.yml` file provided with this course.

## Setting up your conda environment

Here we're assuming you have already installed Miniforge and have opened a terminal window. If you haven't done that yet, please follow the instructions [here](install_python.md).

1. Open your terminal.
	- **Windows**: Open the "Miniforge Prompt" from your start menu
	- **Mac OS**: Open Terminal (you can search for it in spotlight - cmd + space)
	- **Linux**: Open your terminal application

1. The file `environment.yml` (`notebooks` folder) contains the dependencies needed to run the notebooks, and it specifies a `conda` environment named `labcourse-ia`. Create this environment from the file by entering the following command.

	```bash
	conda env create -f https://git.bsse.ethz.ch/scu_courses_public/scu_lab_course_ia/-/raw/main/notebooks/environment.yml
	```

1. Once the environment setup has finished, activate the environment. If you successfully activated the environment, you should now see `(labcourse-ia)` to the left of your command prompt.

	```bash
	conda activate labcourse-ia
	```


1. Test that your notebook installation is working. We will be using notebook for interactive analysis. Enter the command below and it should launch jupyter notebook book in a web browser.

	```bash
	jupyter-lab
	```


## Launching the notebooks

Open your terminal and navigate to the `notebooks` subdirectory of the `scu_lab_course_ia` directory you downloaded.

```
cd scu_lab_course_ia/notebooks
```

Now activate your `labcourse-ia` conda environment you created in the installation step.

```
conda activate labcourse-ia
```

To start the Jupyter Notebook server, enter

```bash
jupyter-lab
```

Jupyter Notebook will open in a browser window and you will see the course notebooks.

## Download pretrained cellpose models

In this course we will use the [cellpose](https://www.cellpose.org/) package for cell segmentation. Cellpose uses pretrained deep learning models for segmentation, which take some time to download the first time you run cellpose. To avoid waiting for the models to download while working through the notebooks, you can download them now by running the following command in your terminal.

```bash
python -c "from cellpose import models; _=models.Cellpose(gpu=False, model_type='cyto')"
```
