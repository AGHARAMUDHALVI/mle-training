import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mle-AGHARAMUDHALVI.C-housing",
    version="v0.3",
    author=" AGHARAMUDHALVI",
    author_email="agharamudhalvi.c@tigeranalytics.com",
    description="A installable housing-package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AGHARAMUDHALVI/mle-training",
   
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)