from setuptools import setup

def preinstall():
    f = open("readme.md","r")
    text = f.read()
    return text

setup(
    name="pythonpackage_morteza",
    version="1.0.0",
    author="mori_cyber",
    description="A package for weight predict based on height ",
    long_description=open("readme.md", 'r').read(),
    requires=[],
    author_email="moridh1355@gmail.com",
    packages=["pythonpackage_morteza"],
    
)
