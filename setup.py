import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iolanta",
    version="0.0.0",
    author="Anatoly Scherbakov",
    author_email="altaisoft@gmail.com",
    description=(
        "Graph with commit log"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/anatoly-scherbakov/iolanta',
    packages=setuptools.find_packages(exclude=[
        'tests',
    ]),
    install_requires=[

    ],
    extras_require={
        'dev': [
            'pytest',
            'fire',
            'twine'
        ]
    },
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
