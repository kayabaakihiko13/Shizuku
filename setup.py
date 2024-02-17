from setuptools import setup

with open("requirements.txt", encoding="utf-8") as file:
    requitments = file.read().splitlines()

setup(
    name="Shizuku",
    version="0.0.1",
    description="Scraping Data Google api With Serpapi",
    packages=["Shizuku"],
    install_requires=requitments,
    python_requires=">=3.10",
    license="MIT License",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
)
