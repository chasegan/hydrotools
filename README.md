# hydrotools" 

## How to install directly from GitHub using pip

https://www.freecodecamp.org/news/how-to-use-github-as-a-pypi-server-1c3b0d07db2/

pip install git+https://github.com/chasegan/hydrotools.git#egg=hydrotools
pip install git+https://github.com/chasegan/hydrotools.git@ver_a#egg=hydrotools
pip install git://github.com/{ username }/{ reponame }.git@{ tag name }#egg={ desired egg name }

Then open python and run these commands:
>>> import hydrotools
>>> hydrotools.__version__

>>> import hydrotools.demo as demo
>>> demo.hello_world()
