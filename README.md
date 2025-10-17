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
  - On Mac
  - On Linux, in the terminal run: ``
2. Create an empty folder "testing-chunter"
3. Download example notebook into your "testing-chunter" folder.
4. In the terminal run
```sh
uv init
uv add chunter
uv add jupyternotebook
uv run jupyter notebook
```
5. The last command should open a new tab in your Browser. This is were you can execute our example notebook. On the left side click on `Capolupo-cell-cyclte.ipynb`.

### Option 2: Run Cocycle Hunter using Conda and Jupyter notebooks

1. We assume that conda is already installed on your computer. If note we recommend using miniforge, please go to the [Miniforge webpage] for an installation Guide.
2. Create an empty folder "testing-chunter"
3. Download example notebook into your "testing-chunter" folder.
4. In the terminal run
```sh
conda create -n cocycle-hunter-env python=3.10 jupyter-notebook
conda activate cocycle-hunter-env
pip install chunter
jupyter-notebook
```

### Run Cocyclte Hunter using UV + VSCode / PyCharme

1. Install UV
2. Create an empty folder
3. Download example notebook into your "testing-chunter" folder.
4. In the terminal run
```sh
uv init
uv add chunter
uv add ipykernel
```
5. Install VSCode or PyCharme
6. Start VSCode / PyCharm and open the folder "testing-chunter"
7. Click on `Capolupo-cell-cycle.ipynb`, press Strg+Enter to execute the first cell. You will be asked for the jupyter kernel to use, select '.venv/bin/python'
