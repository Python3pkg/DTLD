__author__ = 'David Dexter'
import os
from setuptools import setup
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "dtld",
    version = "0.0.1",
    author = "David Dexter",
    author_email = "dmwangimail@gmail.com",
    description = ("Custome Top level domain extractor "),
    license = "BSD",
    keywords = "top level domain extractor",    
    packages=['dtld','lib'],
    
)
