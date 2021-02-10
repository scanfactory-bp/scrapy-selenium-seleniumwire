from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    install_requires=['scrapy==2.3.0', 'selenium==3.141.0', 'selenium-wire==2.1.1']
)
