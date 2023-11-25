# Development
---------------
The source repository is in [GitHub](https://github.com/sanjeevs/golftracker). 
The overall software design is shown below ![ArchDiagram](docs/source/images/sw_top_level.png)

The development flow is similar to other python projects.
* Clone the project.
```
git clone https://github.com/sanjeevs/golftracker.git
```
* Create a virtual env and install all the dependencies
```
venv>  pip install -r requirements.txt
```
* Run unit tests for sanity
```
(venv)golftracker> pytest
```
* Install the package locally for development.
```
 pip install -e .
```

## Distribution
------------------------
For releasing the package to [pypi](https://pypi.org/project/golftracker/)

* Bump the version in setup.py
* Build the distribution
```commandline
python setup.py bdist_wheel
```
* Upload the distribution
```commandline
twine upload dist/*
```

