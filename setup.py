
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GreatPublicationPlanner",
    version="0.0.0",
    author="Alexandre Quenon",
    author_email="aquenon@hotmail.be",
    description="A package to display target publications and allow to choose wisely",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Arkh42/GreatPublicationPlanner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
