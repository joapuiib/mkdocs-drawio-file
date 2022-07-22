from setuptools import setup, find_packages
import os.path

def read(name):
    mydir = os.path.abspath(os.path.dirname(__file__))
    return open(os.path.join(mydir, name)).read()


setuptools.setup(
    name="mkdocs-drawio-file",
    version="1.3.0",
    packages=find_packages(),
    url="https://github.com/onixpro/mkdocs-drawio-file",
    license="MIT",
    author="Sergey Lukin",
    author_email="onixpro@gmail.com",
    description="MkDocs plugin to embed drawio files",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    install_requires=["mkdocs"],
    entry_points={"mkdocs.plugins": ["drawio_file = mkdocs_drawio_file:drawio_file_plugin",]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)