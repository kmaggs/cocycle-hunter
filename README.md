[![](https://github.com/kmaggs/cocycle-hunter/actions/workflows/run_tests.yaml/badge.svg)](https://github.com/kmaggs/cocycle-hunter/actions/workflows/run_tests.yaml)

# Cocycle Hunter

**Author**: Kelly Maggs

**License**: [BSD 3-Clause License](LICENSE)

A Python package for identifying cocycles in single-cell RNA-seq data.

## 🚀 Quick Start

Getting started with Cocycle Hunter is simple:

1. Install the package:
   ```sh
   pip install chunter
   ```
2. Run the example notebook:  
   [Capolupo-cell-cycle.ipynb](https://github.com/kmaggs/cocycle-hunter/blob/main/examples/Capolupo/Capolupo-cell-cycle.ipynb)

If you're new to Python or Jupyter notebooks, don't worry—we've got detailed step-by-step instructions below.

## Step-by-Step Setup Guide

There are many ways to set up Python and run Jupyter notebooks. Choose the option that best fits your workflow:

<details>
<summary> Option 1: Use UV + Juptyer Notebooks for a fast and easy setup.</summary>

### Option 1: UV + Jupyter Notebooks (Recommended)

1. *Install [UV](https://docs.astral.sh/uv/getting-started/installation/)*  
   - *Windows*:
     ```powershell
     powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
     ```
   - *macOS/Linux*:
     ```sh
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```

2. *Create a working folder*:
   ```sh
   mkdir testing-chunter
   cd testing-chunter
   ```

3. *Download the example notebook*  
   Right-click [this link](https://raw.githubusercontent.com/kmaggs/cocycle-hunter/main/examples/Capolupo/Capolupo-cell-cycle.ipynb) and choose “Save Link As…” into your folder.

4. *Install dependencies and launch Jupyter*:
   ```sh
   uv init
   uv add chunter
   uv add notebook
   uv run jupyter notebook # This will open the jupyter notebook interface in your browser.
   ```

5. *Run then example notebook*  
   In your browser, open `Capolupo-cell-cycle.ipynb` and press `Shift + Enter` to step through the code.
</details>

<details>
<summary>Option 2: Use Conda if you're already familiar with it.</summary>

### Option 2: Conda + Jupyter Notebooks

1. *Install Conda*  
   If you don’t have it yet, we recommend [Miniforge](https://github.com/conda-forge/miniforge#install).

2. *Create a working folder*:
   ```sh
   mkdir testing-chunter
   cd testing-chunter
   ```

3. *Download the example notebook*  
   Save [Capolupo-cell-cycle.ipynb](https://raw.githubusercontent.com/kmaggs/cocycle-hunter/main/examples/Capolupo/Capolupo-cell-cycle.ipynb) into your folder.

4. *Create and activate environment*:
   ```sh
   conda create -n cocycle-hunter-env python=3.10 notebook
   conda activate cocycle-hunter-env
   pip install chunter
   jupyter notebook # This will open the jupyter notebook interface in your browser.
   ```

5. *Run then example notebook*  
   Open `Capolupo-cell-cycle.ipynb` in your browser and execute cells with `Shift + Enter`.
</details>

<details>
<summary>Option 3: Use UV + VSCode / PyCharm for a more powerful experience.</summary>

### Option 3: UV + VSCode or PyCharm

1. *Install UV* (see Option 1)

2. *Create a working folder*:
   ```sh
   mkdir testing-chunter
   cd testing-chunter
   ```

3. *Download then example notebook*  
   Save [Capolupo-cell-cycle.ipynb](https://raw.githubusercontent.com/kmaggs/cocycle-hunter/main/examples/Capolupo/Capolupo-cell-cycle.ipynb) into your folder.

4. *Install dependencies*:
   ```sh
   uv init
   uv add chunter
   uv add ipykernel
   ```

5. *Install an IDE*  
   - [VSCode](https://code.visualstudio.com/download) or 
   - [PyCharm](https://www.jetbrains.com/pycharm/)

6. *Run the Example Notebook in your IDE*  
   Launch your IDE - VSCode or PyCharm. In the main menu click "File > Open Folder..." and the select the "testing-chunter" folder. Now, in the left sidebar, click on "Capolupo-cell-cycle.ipynb". This will open the example notebook. Click right below the title "Cell cocycle analysis in Capolupo ..." and press `Shift + Enter`. A popup window should appear and ask you to select a kernel. Click on "Python Environments..." and afterwards click on "testing-chunter .venv/bin/python". Not everything is setup. And you can press `Shift + Enter` to execute the example notebook step by step.
</details>
