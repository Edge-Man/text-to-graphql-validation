import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graphqlval", # Replace with your own username
    version="0.0.1",
    author="Andre Carrera",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/acarrera94/text-to-graphql-validation",
    packages=setuptools.find_packages(),
    dependency_links=['git+https://github.com/acarrera94/graphql-core@37044c820ffe505e26a7c84a66576ee8d2690e1e#egg=graphql-core'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
