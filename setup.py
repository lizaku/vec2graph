import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vec2graph",
    version="0.0.1",
    author="Nadezda Katricheva, Alyaxey Yaskevich, Anastasiya Lisitsina, Tamara Zhordaniya, "
           "Andrey Kutuzov, Elizaveta Kuzmenko",
    author_email="lizaku77@gmail.com",
    description="Mini-library for producing graph visualizations from embedding models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lizaku/vec2graph",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
