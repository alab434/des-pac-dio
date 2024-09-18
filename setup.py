from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="mynomar",
    version="0.0.1",
    author="Almyr P.",
    author_email="my_email@example.com",
    description="Normaliza nomes de arquivos.",
    readme='README.md',
    long_description=page_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.10',
    install_requires=requirements,
    packages=find_packages(),
    url="https://github.com/alab434/des-pac-dio",
)
