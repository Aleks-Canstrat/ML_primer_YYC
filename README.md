# Geocomputing & machine learning course

[Agile Scientific](www.agilescientific.com)
 
This is a crash course in the fundamentals of [Python](https://www.python.org/) programming and scientific computing with applications in geoscience. We deliver the course by alternating short tutorials with hands-on programming exercises. As a participant, you will get practice with programming syntax by following along on their laptops. You will receive the entire set of presentations, programs, and course data at the start of the course, which amounts to a huge amount of working code that you'll be able to make use of by the end of the course.

The course uses standard industry data such as well logs, horizons, and seismic to illustrate computational concepts we all encounter in our daily workflows. We teach using the Python programming language. It's a fun, powerful language for scientific computing. It is easy-to-learn, even if it does have a rather daunting ecosystem of thousands of open source code libraries. But fear not, we'll get you set up and well practiced with the handful of ones that you'll use the majority of the time.

**Instructors:** [Evan Bianco](https://twitter.com/EvanBianco) and [Diego Castañeda](https://twitter.com/dfcastap)

**When**: 3–5 Oct 2017, 8:00 am to 4:00 pm.

**Where**: Aramco Research offices, Houston, Texas.

**Bring**: Participants must bring their **own computers** (Mac, Windows, or Linux) with the required **software already installed** (see **What to install** section (below). [Contact the instructors](https://agilescientific.com/contact-us/) if you need any help **before** the course. 


## <a name="What2Install"></a>What to install

**Please install all software BEFORE coming to the course.** If you have any problems installing or don't know which versions you need to download, get in touch.

### 1. Python
There are many ways to get Python on your system and it can be very confusing when you're first starting out.

I **don't** recommend downloading it from python.org or using the Python that came with your system (common on Linux). Instead, **use the Anaconda distribution**. It will come with all the libraries you need and doesn't require administrator access to install.

Go to https://www.continuum.io/downloads and select the **Python 3.6, 64-bit** version of the installer for your system. Accept the license and accept the default location for Anaconda. When it asks about changing your 'path' to include Anaconda, say "Yes" (be careful — the default is "No").

**Even if you already have Python** (say from your system package manager or ArcGIS, etc), I recommend that you install Anaconda to avoid problems with versioning.

### 2. A text editor
You'll also need a **text editor**. If you don't already have one, I recommend installing [Sublime Text](https://www.sublimetext.com/)
(it's available for Linux, Windows, and Mac). Atom and Notepad++ (for Windows) are also good. If you're looking for a text editor packed full of features and extensions [Visual Studio Code](https://code.visualstudio.com/) is a good alternative to Sublime.


### 3. Git
This next step is optional, but I recommend installing the **git** version control system. This will make it easier to clone the course content and keep it up to date. You may also wish to set up a GitHub account for yourself if you don't already have one. Don't worry if you aren't familiar with git or GitHub. We'll have the course materials on a USB drive that we can transfer to your local machine. Install git by [following their instructions](https://www.atlassian.com/git/tutorials/install-git), or by running `conda install git` after installing Anaconda.


## Learning objectives

By the end of the course, you will be able to:

- Get up and running with state of the art scientific computing software
- Learn the fundamentals of programming common to all programming languages.
- Exposure to general purpose power tools, and geoscience-specific Python code libraries
- Learn how and when to use other people's code, and when to write your own.
- Create stunning 2D and 3D visualizations and graphics that are reproducible, customizable, and transparent.
- Practice wrangling petroleum-specific digital data sets
- Format geoscience data sets to feed into a machine learning pipeline
- Explore, inspect, clean, and engineer new features for machine learning
- Describe the key differences between various machine-learning models.
- Understand the key metrics for assessing the quality and performance of a given model, and how to improve results.
- Define paths of continued learning and future projects


## Recommended literature

Other great places to pick up Python:

- [A Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython) – The essentials from the essential Jake Vanderplas.
- [Learn X in Y minutes](https://learnxinyminutes.com/docs/python3/) — If you just want to get cracking.
- [Stavros](https://www.stavros.io/tutorials/python/) — If you want to know a bit more.
- [Robert Johansson's lectures](Lecture-1-Introduction-to-Python-Programming.ipynb)
- [Tutorials Point](http://www.tutorialspoint.com/python/python_quick_guide.htm) — Another option.
- [Code Academy](https://www.codecademy.com/learn/python) — A more sedate pace.
- [Udacity Intro to Computer Science](https://www.udacity.com/course/intro-to-computer-science--cs101) — Fantastic but a serious undertaking.
- [All the tutorials!](https://wiki.python.org/moin/BeginnersGuide/Programmers)
- [Agile Scientific blog posts featuring executable code](https://agilescientific.com/courses/) – Scroll down to the bottom to find a list of links. 
- [Agile's: x-lines of Python series](https://github.com/agile-geoscience/xlines/tree/master/notebooks) – GitHub repo of notebooks doing something neat in less than X lines of code (where x < 10 or so).

**WARNING** There's still a lot of Python 2 around. Keep away from it if you can! Python 3 has lots of advantages, and there are hardly any libraries now that have not made the swtich.


## Other things

* [Learn everything about IPython and the Notebook!](https://nbviewer.jupyter.org/github/ipython/ipython/blob/master/examples/IPython%20Kernel/Index.ipynb) There's a lot to know, but some of it seems a bit un-Pythony to me.
* [A really awesome series of notebooks about Python.](http://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/tree/master/)
* [Some gentle introductions to Git](https://gist.github.com/jaseemabid/1321592)


## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This content is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
