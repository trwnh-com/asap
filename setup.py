from setuptools import setuptools

with open("README", 'r') as f:
  long_description = f.read()

setup(
  name="asap",
  version="0",
  description="",
  long_description=long_description,
  license="Public Domain",
  author="trwnh",
  author_email="a@trwnh.com",
  url="https://github.com/trwnh-com/asap",
  packages=["asap"],
)