from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

long_description = """FastAPI service to process QA requests."""

requirements_list = [
    "fastapi==0.72.0",
    "uvicorn"
]


setup(
    name="codingchallenge-qa-service",
    version="1.0.0",
    license="UNLICENSED",
    description="Syntea Coding Challenge: QA Service",
    long_description=long_description,
    author_email="Synthetic Teaching - IU Group GmbH",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    python_requires=">=3.9",
    install_requires=requirements_list,
    zip_safe=False,
)
