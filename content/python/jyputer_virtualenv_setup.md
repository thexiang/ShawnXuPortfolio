Title: Jupyter virtualenv setup
Date: 2019-10-07
Category: Python
Tags: Jupyter


## Setup
1. Install Anaconda for Python 3.7 for your operating system: [Anaconda](https://www.anaconda.com/download/)
2. Create a directory/folder for data science and move into it.
3. Download [environment.yml](https://gist.github.com/actsasgeek/5a384af2c7fd7b4c782a3f2b4bc2fdc4) 
4. Execute `conda env create -f environment.yml`
5. You now have all the libraries listed in environment.yml
6. Set up Jupyter notebook to use this environment:
`python -m ipykernel install --user --name <env_name> --display-name "Python <env_name>"`

For now, the only thing in this directory will be the `environment.yml` file.

## Workflow

1. `conda activate <env_name>` - this will activate the environment. (Use `conda env list` to see your installed environments).
2. `jupyter notebook` - this will start the Jupyter notebook environment with the current directory as the root.
3. When you create a new Jupyter notebook, you can select "Python `<env_name>`" as the kernel.

When you're done, you can invoke `conda deactivate`.


## Common issue
`jupyter notebook` deson't work, it's probabbly notebook isn't installed in the virtual env
```
conda install notebook
```