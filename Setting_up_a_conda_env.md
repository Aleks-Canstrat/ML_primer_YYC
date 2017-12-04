### 3. Setting up a virtual environment ###

[Good tutorial](https://tdhopper.com/blog/2015/Nov/24/my-python-environment-workflow-with-conda/) From Tim Hopper 

A virtual environment is a named, isolated, self-contained, working copy of Python that maintains its own files, directories, and paths so that you can work with specific versions of Python code libraries without affecting other Python projects that you may or may not have on your machine. Virtual enviroments make it easy to cleanly separate different projects and avoid problems with different dependencies and version numbers for different software components. 

Once you've installed Anaconda, open a terminal, and create a [virtual environment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/) for the course using the `conda` command:

### 1. Check conda is installed and in your PATH ###
1. Open a terminal
2. Enter `conda -V` into the terminal command line and press enter.
3. If conda is installed you should see something like the following.
```
$ conda -V 
conda 3.7.0
```
### 2. Check conda is up to date ###
1. in the terminal, enter
```
conda update conda
```
2. update any packages by pressing `y` to proceed

### 3. Create a virtual environment for your project ###

1. In the terminal client, in order to create a virtual environment called `your_environment` enter the following where `your_environment` is the name you want to call your environment, and replace x.x with the Python version you wish to use. (To see a list of available python versions first, type `conda search "^python$"` and press enter.)

```conda create -n your_environment python=x.x anaconda```

For instance, to create a virtual environment called `geocomputing` with Python version 3.6 type,

```conda create -n geocomputing python=3.6 anaconda```

2. Press `y` to proceed. This will install the Python version and all the associated anaconda packaged libraries at “path_to_your_anaconda_location/anaconda/envs/yourenvname”

### 4. Activate your virtual environment ###

To activate or switch into your virtual environment, simply type the following where yourenvname is the name you gave to your environement at creation.
```
source activate geocomputing
```
Activating a conda environment modifies the PATH and shell variables to point to the specific isolated Python set-up you created. The command prompt will change to indicate which conda environemnt you are currently in by prepending `(geocomputing)`. To see a list of all your environments, use the command `conda info -e`.

### 5. Install additional Python packages to a virtual environment. ###

To install additional packages only to your virtual environment, enter the following command where *yourenvname* is the name of your environemnt, and *[package]* is the name of the package you wish to install. Failure to specify “-n yourenvname” will install the package to the root Python installation.

```conda install -n yourenvname [package]```

```conda install -n geocomputing obspy```

```conda install -n geocomputing bruges```



### 6. Deactivate your virtual environment. ###

To end a session in the current environment, enter the following. There is no need to specify the envname - which ever is currently active will be deactivated, and the PATH and shell variables will be returned to normal.
```source deactivate```

### 7. Delete a no longer needed virtual environment ###

To delete a conda environment, enter the following, where yourenvname is the name of the environment you wish to delete.
```conda remove -n yourenvname -all```


