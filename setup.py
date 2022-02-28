from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="john_community_modules",
    version="1.0",
    description="Module provides new john modules created by john community",
    license="GPL 2.0",
    long_description=long_description,
    author="Grzegorz Gajewski",
    author_email="...",
    packages=find_packages(),
    install_requires=["setuptools", "wheel"],
)
