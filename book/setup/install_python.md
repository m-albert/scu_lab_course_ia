# Installing Python

## Overview

To run the Python jupyter notebooks used in this course, you need to install Python locally on your computer.

We use `pixi` to install Python and the packages needed for the course. Pixi creates the course environment from the `pixi.toml` and `pixi.lock` files in this repository, so everyone uses the same tested package versions.

```{admonition} What is Pixi?
`pixi` is an environment and package manager for scientific software. In this course it installs Python, JupyterLab, image-analysis packages, Java, and the remaining tools needed by the notebooks.
```

## Instructions

Select the installation instructions for your operating system from the tabs below.

::::{tab-set}
:::{tab-item} Linux and macOS
1. Open your terminal application.
1. Install Pixi:

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

1. Close the terminal window and open a new one.
1. Check that Pixi is available:

```bash
pixi --version
```
:::

:::{tab-item} Windows
1. Open PowerShell.
1. Install Pixi:

```powershell
powershell -ExecutionPolicy Bypass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

1. Close PowerShell and open it again.
1. Check that Pixi is available:

```powershell
pixi --version
```
:::
::::

If the installer is blocked on your computer, you can also install Pixi using a system package manager such as Homebrew, Winget, or Scoop. The official installation page lists these alternatives.
