from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    install_requires=get_requirements('requirements/requirements.txt')
)
