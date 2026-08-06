# Setting up a Python environment

Running the notebooks in this course requires a Python environment with the necessary packages installed. This section explains how to set up the course environment using Pixi.

## Setting up your Pixi environment

Here we're assuming you have already installed Pixi and have opened a terminal window. If you haven't done that yet, please follow the instructions [here](install_python.md).

1. Open your terminal.
   - **Windows**: Open PowerShell
   - **Mac OS**: Open Terminal (you can search for it in spotlight - cmd + space)
   - **Linux**: Open your terminal application

1. Navigate to the course folder. This is the folder that contains the `pixi.toml` and `pixi.lock` files.

   ```bash
   cd path/to/scu_lab_course_ia
   ```

1. Install the environment:

   ```bash
   pixi install
   ```

   The first installation can take several minutes because Pixi downloads Python, scientific packages, Java, and JupyterLab.

1. Test that your notebook installation is working. Enter the command below and it should launch JupyterLab in a web browser.

   ```bash
   pixi run jupyter lab
   ```

JupyterLab will open in a browser window. If this worked, you can close the browser window again and stop the notebook server by going back to your terminal and pressing `CTRL-C` twice. Possibly, you will be asked to confirm that you want to shut down the server by entering `y` and pressing `ENTER`.

You do not need to activate the environment manually. Use `pixi run` from the course folder whenever you want to run a command inside the course environment.

## Optional: using a Pixi shell

If you want to run several commands in the course environment, you can start an interactive Pixi shell:

```bash
pixi shell
```

While this shell is active, commands such as `python`, `pytest`, or `jupyter lab` use the course environment directly. Type `exit` to leave the shell and return to your normal terminal.
