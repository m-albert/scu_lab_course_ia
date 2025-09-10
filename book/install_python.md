# Optional: Installing Python

## Overview

Day 1 of this course introduced python and jupyter notebooks. This part of the course will focus on practical image processing with Python. To run the jupyter notebooks used in this course, you can use a python installation
- on your computer or
- on the virtual BAND computers provided with this course.

For both of these options, we recommend using `conda` to manage your python environment. If not already done, you can install conda following the instructions below.


    ```{admonition} What is conda?
    `conda` is a very commonly used environment and package manager which makes python and related software packages available on your computer.


## Instructions

Select the installation instructions for your operating system and processor from the tabs below.

````{tab-set}
```{tab-item} Linux (e.g. BAND)
1. In your web browser, navigate to this [download page](https://github.com/conda-forge/miniforge#miniforge).
2. Scroll down to the "Miniforge3" header of the "Downloads" section. Click the link to download link for `Miniforge3-Linux-x86_64`.
3. Open your terminal application
4. Navigate to the folder you downloaded the installer to (usually this is in your Downloads folder). If the file was downloaded to your Downloads folder, you would enter:

    ```bash
    cd ~/Downloads
    ```
5. Execute the installer with the command below. You can use your arrow keys to scroll up and down to read the license agreement and enter "yes" if you agree.

    ```bash
    bash Miniforge-Linux-x86_64.sh
    ```

6. After installation, you will be asked if you would like to initialize your terminal with "conda init". For a local installation, you enter "yes" here and the conda command will be available every time you open a terminal. In this course, we work on virtual BAND computers, and in this case we enter "no".

7. To verify your installation worked, close your Terminal window and open a new one. You should see `(base)` to the left of your prompt.


    ```{admonition} You were already seeing (base)?
    If you said "no" in the previous point, activate the conda command in your terminal by entering the following in the terminal:


    ```bash
    source ~/miniforge3/bin/activate
    ```

```

```{tab-item} Mac OS (Intel)
1. In your web browser, navigate to this [download page](https://github.com/conda-forge/miniforge#miniforge).
2. Scroll down to the "Miniforge" header of the "Downloads" section. Click the link to download link for `Miniforge-MacOSX-x86_64`.
3. Open your Terminal (you can search for it in spotlight - `cmd` + `space`)
4. Navigate to the folder you downloaded the installer to (usually this is in your Downloads folder). If the file was downloaded to your Downloads folder, you would enter:

    ```bash
    cd ~/Downloads
    ```
    
5. Execute the installer with the command below.  You can use your arrow keys to scroll up and down to read the license agreement and enter "yes" if you agree.

    ```bash
    bash Miniforge-MacOSX-x86_64.sh
    ```

6. After installation, you will be asked if you would like to initialize your terminal with "conda init". Enter "yes" to initalize your terminal.   
7. To verify your installation worked, close your Terminal window and open a new one. You should see `(base)` to the left of your prompt.
    
    ```{admonition} Don't see (base)?
    You can manually initialize conda by entering the command below and re-opening your terminal application.

    ```bash
    conda init
    ```

```

```{tab-item} Mac OS (M1/M2)
1. In your web browser, navigate to this [download page](https://github.com/conda-forge/miniforge#miniforge).
2. Scroll down to the "Miniforge" header of the "Downloads" section. Click the link to download link for `Miniforge-MacOSX-arm64`.
3. Open your Terminal (you can search for it in spotlight - `cmd` + `space`)
4. Navigate to the folder you downloaded the installer to (usually this is in your Downloads folder). If the file was downloaded to your Downloads folder, you would enter:

    ```bash
    cd ~/Downloads
    ```
    
5. Execute the installer with the command below. You can use your arrow keys to scroll up and down to read it/agree to it.

    ```bash
    bash Miniforge-MacOSX-arm64.sh
    ```
    
6. After installation, you will be asked if you would like to initialize your terminal with "conda init". Enter "yes" to initalize your terminal. 
7. To verify your installation worked, close your Terminal window and open a new one. You should see `(base)` to the left of your prompt.

    ```{admonition} Don't see (base)?
    You can manually initialize conda by entering the command below and re-opening your terminal application.

    ```bash
    conda init
    ```

```

```{tab-item} Windows
1. In your web browser, navigate to this [download page](https://github.com/conda-forge/miniforge#miniforge).
2. Scroll down to the "Miniforge" header of the "Downloads" section. Click the link to download link for `Miniforge-Windows-x86_64`.
3. Find the file you downloaded (Miniforge-Windows-x86_64.exe) and double click to execute it. Follow the instructions to complete the installation.
4. Once the installation has completed, you can verify it was correctly installed by searching for the "miniforge prompt" in your Start menu.
```
````