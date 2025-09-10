# Setting up a python environment

Running the notebooks in this course requires a python environment with the necessary packages installed. This section explains how to set up the right environment using `conda` and the `environment.yml` file provided with this course.

## Setting up your conda environment

Here we're assuming you have already installed Miniforge and have opened a terminal window. If you haven't done that yet, please follow the instructions [here](install_python.md).

1. Open your terminal.
	- **Windows**: Open the "Miniforge Prompt" from your start menu
	- **Mac OS**: Open Terminal (you can search for it in spotlight - cmd + space)
	- **Linux**: Open your terminal application


2. Navigate to the `notebooks` subdirectory of the Image Analysis Lab Course materials you downloaded.

	```bash
	cd lab_course_ia_materials/notebooks
	```


3. The file `environment.yml` contains the dependencies needed to run the notebooks, and it specifies a `conda` environment named `lab_course_ia`. Create this environment from the file by entering the following command.

	```bash
	conda env create --file environment.yml
	```

4. Once the environment setup has finished, activate the environment. If you successfully activated the environment, you should now see `(lab_course_ia)` to the left of your command prompt.

	```bash
	conda activate lab_course_ia
	```


5. Test that your notebook installation is working. We will be using notebook for interactive analysis. Enter the command below and it should launch jupyter notebook book in a web browser.

	```bash
	jupyter-lab
	```


## Launching the notebooks

Open your terminal and navigate to the `notebooks` subdirectory of the `lab_course_ia_materials` directory you downloaded.

```
cd lab_course_ia_materials/notebooks
```

Now activate your `lab_course_ia` conda environment you created in the installation step.

```
conda activate lab_course_ia
```

To start the Jupyter Notebook server, enter

```bash
jupyter-lab
```

Jupyter Notebook will open in a browser window and you will see the course notebooks.
