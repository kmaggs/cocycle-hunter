# Cocycle Hunter

Python package for hunting for cocycles in single-cell RNA-seq data.

## Getting Started

Using Cocycle Hunter is just as easy as any other python package:
1. Install Chunter via pip:
    ```sh
    pip install chunter
    ```
2. Run our example notebook:

   [Capolupo-cell-cycle.ipynb](https://github.com/kmaggs/cocycle-hunter/blob/main/examples/Capolupo/Capolupo-cell-cycle.ipynb). 

For people that are new to python and jupyter notebooks. Below are some more detailed step by step instruction.

## Step-by-Step Instructions

There are countless ways to setup python and to work with jupyter notebooks. The first option below, might be the simples way run our example notebook on your computer.
If you often work with Conda, option 2 is for you. But we would recommend you trying UV as package manager. It is faster, easier, reliable and less error prone than conda.
Finally if you would like a powerful IDE that lets you work efficiently with jupyter notebooks that try option 3. 

### Option 1: Run Cocycle Hunter using UV and Jupyter notebooks

1. Install UV as described on the UV web page.
  - On Windows, open PowerShell and execute: 
    ```shell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
  - On MacOS and Linux, in the terminal run: ``
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    
2. Create an empty folder "testing-chunter"
3. Download  into your "testing-chunter" folder. Follow [this link](https://github.com/kmaggs/cocycle-hunter/blob/main/examples/Capolupo/Capolupo-cell-cycle.ipynb) and then click:
   
   TODO
   
4. In the terminal run
    ```sh
    cd testing-chunter
    uv init
    uv add chunter
    uv add notebook
    uv run jupyter notebook
    ```
5. The last command should open a new tab in your Browser. Click on `Capolupo-cell-cyclte.ipynb`, to open the notebook. Click `Shift + Enter` many times to execute the notebook step by step.

### Option 2: Run Cocycle Hunter using Conda and Jupyter notebooks

1. We assume that conda is already installed on your computer. If not, we recommend using Miniforge, please go to the [Miniforge webpage](https://github.com/conda-forge/miniforge#install) for an installation guide.
2. Create an empty folder "testing-chunter"
3. Download [example notebook](https://github.com/kmaggs/cocycle-hunter/blob/main/examples/Capolupo/Capolupo-cell-cycle.ipynb) into your "testing-chunter" folder.
4. In the terminal run
    ```sh
    cd testing-chunter
    conda create -n cocycle-hunter-env python=3.10 notebook
    conda activate cocycle-hunter-env
    pip install chunter
    jupyter notebook
    ```

### Option 3: Run Cocyclte Hunter using UV + VSCode / PyCharm

1. Install UV (see [webpage](https://docs.astral.sh/uv/getting-started/installation/))
   - On Windows, open PowerShell and execute:
     ```shell   
     powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"   
     ```   
   - On MacOS and Linux, in the terminal run: ``   
     ```sh   
     curl -LsSf https://astral.sh/uv/install.sh | sh   
     ```   
2. Create an empty folder "testing-chunter"
3. Download [example notebook]((https://github.com/kmaggs/cocycle-hunter/blob/main/examples/capolupo/capolupo-cell-cycle.ipynb) into your "testing-chunter" folder.
4. In the terminal run

    ```sh
    cd testing-chunter
    uv init
    uv add chunter
    uv add ipykernel
    ```

5. Install [VSCode](https://code.visualstudio.com/download) or [PyCharm](https://www.jetbrains.com/pycharm/)
6. Start VSCode / PyCharm and open the folder "testing-chunter"
7. Click on `Capolupo-cell-cycle.ipynb`, press `Shift + Enter` many times to execute the notebook step by step.
