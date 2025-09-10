<!---

BSD License

Copyright (c) 2022, Kevin Yamauchi
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from this
  software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.

-->

# Optional: Setting up a python environment

Running the notebooks in this course requires a python environment with the necessary packages installed. This section explains how to set up the right environment using `conda` and the `environment.yml` file provided with this course.

If you use the [virtual BAND computers](https://band.vm.fedcloud.eu), you can use the pre-installed environment `EuBi Course` to run the notebooks. If you are using your own computer (or want to practice setting up your own environment), you can follow the instructions below.


## Setting up your conda environment

Here we're assuming you have already installed miniforge and have opened a terminal window. If you haven't done that yet, please follow the instructions [here](install_python.md).

1. Open your terminal.
	- **Windows**: Open the "miniforge prompt" from your start menu
	- **Mac OS**: Open Terminal (you can search for it in spotlight - cmd + space)
	- **Linux**: Open your terminal application


2. Navigate to the `notebooks` subdirectory of the `bioimage_analysis_with_python_course` directory you downloaded.

	```bash
	cd 20241008_remote_python_bioimage_analysis_course_day2/notebooks
	```


3. The file `environment.yml` contains the dependencies needed to run the notebooks, and it specifies a `conda` environment named `env_day2`. Create this environment from the file by entering the following command.

	```bash
	conda env create --file environment.yml
	```

4. Once the environment setup has finished, activate the environment. If you successfully activated the environment, you should now see `(env_day2)` to the left of your command prompt.

	```bash
	conda activate env_day2
	```


5. Test that your notebook installation is working. We will be using notebook for interactive analysis. Enter the command below and it should launch jupyter notebook book in a web browser.

	```bash
	jupyter-lab
	```


## Launching the notebooks

Open your terminal and navigate to the `notebooks` subdirectory of the `20241008_remote_python_bioimage_analysis_course_day2` directory you downloaded.

```
cd 20241008_remote_python_bioimage_analysis_course_day2/notebooks
```

Now activate your `env_day2` conda environment you created in the installation step.

```
conda activate env_day2
```

To start the Jupyter Notebook server, enter

```bash
jupyter-lab
```

Jupyter Notebook will open in a browser window and you will see the course notebooks.
