import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hydrotools",
    version="0.0.1",
    author="Chas Egan",
    author_email="thecosmologist@gmail.com",
    description="A code torrent of washing sprawl which in watery worlds is able of all.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chasegan/hydrotools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)