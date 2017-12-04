# Geoscience Machine Learning course curriculum
***
## Part 1: Introduction to Python

On the first day we will get used to Python's syntax and built-in functions, and explore the rich world of NumPy and SciPy. At the end of the day, we will have a good overview of the basic toolset used by earth scientists everywhere, and be ready to dive deeper. 

### Manipulating and visualizing data 
- **Follow-along exercise: Make a topography map in 5 lines of code**
- **Follow-along exercise: A lightweight 3D seismic visualization.**

### Variables and assignment
- Introduction to Python command line.
- Basic assignment syntax and dynamic typing.
- Asking for help. Finding help online.

### Native data types
- `int` and `float` (and `complex` and `long`); why so many kinds of numbers?
- `str`.
- Type casting.
- String methods, strings as collections. Indexing and slicing.
- String formatting.
- **Exercise: text processing practice manipulating formation names.**
- **Exercise: manipulating text to build geologic descriptions**

### Operators and expressions

- Mathematical operations, comparison operators, booleans.
- Augmented assignment, multiple assignment.
- Copies and pointers.
- **Exercise: some gentle rock physics.**

### Data collections and data structures
- `list` — indexing again, slicing again, striding, nested lists.
- **Exercise: Getting ages from the geologic timescale. Practice indexing.**
- `dict` — probably the most important data structure in Python.
- **Exercise: Stratigraphic column: practice storing, retrieving and modifying entries in dictionaries.**
- **Exercise: Introduction to visualizing well logs. Line plots and color-coded scatter plots.**
- `tuple` and `set`


### Flow control
- Iteration and iterables: `for` and `while`.
- **Exercise: compute impedance and reflectivity in a well.** 
- List comprehension.
- Exercise: convert `for` loops into list comprehensions.
- Making decisions: `if–elif–else` statements.
- **Exercise: create a pay flag on a gamma-ray log.**

### Getting data
- Reading text files.
- **Exercise: create a dictionary of well tops from a ‘broken’ input text file.**

***
## Part 2: Intro to scientific computing
On day two we will get into the practical aspects of scientific computing with Python. We'll look at data loading, writing new files, functions, and some of the building blocks of real applications. After Day 2, students will have some understanding of how to make useful scientific tools.

### Functions
- Built-in functions, and importing modules.
- The anatomy of a function. Syntax, docstrings.
– **Exercise: write a function that calculated Vshale from a Gamma Ray log.**
- **Exercise: write a function that computes an impedance log.**
- **Exercise: write a function that computes reflection coefficients.**
- **Exercise: write a function that returns a tops dictionary.**
- **Exercise: write a function that computes formation thicknesses.**
- Sharing code via modules.
- Importing and using modules.
- **Exercise: Getting data from a sidewall core analysis report (csv file).**
- **Exercise: Get geological ages by processing pages.**
- The Python standard library.
- **External Python packages — PyPi, Numpy, Matplotlib, SciPy, Pandas, etc.**

### NumPy
- Load and inspect a 1D wireline log.
- **Exercise: compare list iteration to vectorized math.**
- Load and inspect a 2D seismic section from Numpy binary.
- **Exercise: plotting raster data with imshow.**
- Load and inspect a 3D seismic volume from Numpy binary.
- Indexing into the cube, computing trace statistics.
- Visualize traces, sections, and timeslices.
- **Exercise: load and visualize a seismic horizon.**

### SciPy
- Complex trace attributes — phase and envelope.
- Moving window attributes — RMS energy.
- Multi-trace attributes — semblance
- Spectral decomposition.
- **Exercise: calculate the Power Spectrum of seismic data**
- **Exercise: make a simple synthetic seismogram.**

### Reading and writing data files
- Using ObsPy to read SEG-Y, welly to read LAS.
- Writing SEG-Y and LAS files.
- Reading and writing SHP files with fiona.
- A quick introduction to GeoPandas.
- Classes (time permitting)
- Everything is an object.
- Why use classes?
- **Exercise: define a well log class with attributes and methods.**
- Command line tools (time permitting)
- Running Python programs: review.
- Getting arguments from the command line.

***
### Part 3: Intro to machine learning
On the last day, we'll explore the Pandas and Scikit Learn packages for simple machine learning tasks using geoscience data examples. After this day, students will have a good overview of how to look at large datasets and solve problems with state-of-the-art machine learning tools.
- Machine learning concepts
- What is it that you’re trying to solve? How can machine learning help?
- What's the difference between supervised and unsupervised methods?
- What's the difference between classification and regression?
- What is artificial intelligence, and what is deep learning?

### Data management for machine learning
- DataFrames: A new way to look at well logs.
- **Exercise: loading a DataFrame from a CSV.**
- **Exercise: building a DataFrame from LAS file.**
- DataFrames vs arrays (vs Hadoop, Dask, or what-have-you).

### The machine learning iterative loop
- Data — Getting the data. How to load it and put it in an `array` and/or `DataFrame`
- Processing — data exploration, inspection, cleaning, and feature engineering.
- Model – What is a model? Training a Scikit-Learn model (for now).
- Results – assessing quality and performance metrics (accuracy, recall, F1, confusion matrices)
- Repeat – What can we do to improve performance?
- **Exercise: predicting a missing well log.**
- **Exercise: improving the pay flag prediction.**
- **Exercise: Hugoton lithology prediction contest.**
- **Exercsise: something to do with seismic.**