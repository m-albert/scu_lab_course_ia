# Setting up a python environment

Running the notebooks in this course requires a python environment with the necessary packages installed. This section explains how to set up the right environment using `conda` and the `environment.yml` file provided with this course.

## Setting up your conda environment

Here we're assuming you have already installed Miniforge and have opened a terminal window. If you haven't done that yet, please follow the instructions [here](install_python.md).

1. Open your terminal.
	- **Windows**: Open the "Miniforge Prompt" from your start menu
	- **Mac OS**: Open Terminal (you can search for it in spotlight - cmd + space)
	- **Linux**: Open your terminal application

1. The file `environment.yml` (`notebooks` folder) contains the dependencies needed to run the notebooks, and it specifies a `conda` environment named `labcourse-ia`. Create this environment from the file by copy pasting the following command (for convenvience, the environment file was made available online):

	```bash
	conda env create -f https://gist.githubusercontent.com/m-albert/9d3d6af1051b35c92d1c7a56bd193560/raw/ac8c0aa071073794d2ec7f8ca31755917a5f4e9f/labcourse-ia-environment.yml
	```

1. Once the environment setup has finished, activate the environment. If you successfully activated the environment, you should now see `(labcourse-ia)` to the left of your command prompt.

	```bash
	conda activate labcourse-ia
	```


1. Test that your notebook installation is working. We will be using notebook for interactive analysis. Enter the command below and it should launch jupyter notebook book in a web browser.

	```bash
	jupyter-lab
	```

Jupyter Notebook will open in a browser window. If this worked, you can close the browser window again and stop the notebook server by going back to your terminal and pressing `CTRL-C` twice. Possibly, you will be asked to confirm that you want to shut down the server by entering `y` and pressing `ENTER`.
