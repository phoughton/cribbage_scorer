import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cribbage_scorer",
    version="0.2.0",
    author="Peter Houghton",
    author_email="pete@investigatingsoftware.co.uk",
    description="A Cribbage scoring tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phoughton/cribbage_scorer",
    packages=setuptools.find_packages(),
    install_requires=[
          'more-itertools',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)