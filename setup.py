import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vec2graph",
    version="0.2.4",
    author="Nadezda Katricheva, Alyaxey Yaskevich, Anastasiya Lisitsina, Tamara Zhordaniya, "
           "Andrey Kutuzov, Elizaveta Kuzmenko",
    author_email="andreku@ifi.uio.no",
    description="Mini-library for producing graph visualizations from embedding models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lizaku/vec2graph",
    packages=setuptools.find_packages(),
    package_data={'vec2graph': ['data/genviz.html', 'data/genviz.js']},
    python_requires='>=3',
    install_requires=['gensim>3.5', 'smart_open>1.8', 'requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Utilities"
    ],
)
