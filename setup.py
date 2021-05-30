import setuptools
import os

HERE = os.path.dirname(__file__)

with open(os.path.join(HERE, "README.md"), "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycraft",  # Replace with your own username
    version="0.1.0",
    author="Simon Ditner and Mike C. Fletcher",
    author_email="mcfletch@vrplumber.com",
    description="Automated dockerised Python-for-Minecraft (PycraftServer) server setup with API samples and live coding in text chat",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mcfletch/pycraft",
    packages=setuptools.find_packages(
        '.',
        exclude=('tests',),
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'pycraft-chat-server = pycraft.achatserver:main',
            'pycraft-channel-test = pycraft.server.operations:main',
        ]
    },
    python_requires='>=3.6',
)