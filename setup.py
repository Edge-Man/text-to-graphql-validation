import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graphqlval",  # Replace with your own username
    version="0.0.1",
    author="Andre Carrera",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/acarrera94/text-to-graphql-validation",
    packages=setuptools.find_packages(),
    install_requires=['graphql-core @ git+https://github.com/acarrera94/graphql-core@handle_sets#egg=graphql-core'],
    python_requires='>=3.6',
)
