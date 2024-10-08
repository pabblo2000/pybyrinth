from setuptools import setup, find_packages

setup(
    name="pyyrinth",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[],  
    author="Pablo Álvaro Hidalgo",
    author_email="palvaroh2000@gmail.com",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tu_usuario/tu_proyecto",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
