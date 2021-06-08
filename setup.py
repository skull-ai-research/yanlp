import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="yanlp",
  version="0.0.1",
  author="skull.ai.research",
  author_email="skull.ai.research@gmail.com",
  description="yannlp",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/skull-ai-research/yanlp",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)
