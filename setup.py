from setuptools import find_packages, setup

setup(
    name = "DS-Project1",
    version = "0.1.0",
    author = "Akib",
    author_email = "ahsanakib3567@gmail.com",
    packages = find_packages(),
    install_requires = ['pandas', 'numpy', 'scikit-learn', 'matplotlib', 'seaborn']
)