from setuptools import setup, find_packages

setup(
    name="hairBrushDetection", 
    version="0.0.0", 
    author="ebrahim", 
    author_email="ebid.py@gmail.com", 
    package_dir={"": "src"}, 
    packages=find_packages(where="src/"), 
    install_requires=[]
)