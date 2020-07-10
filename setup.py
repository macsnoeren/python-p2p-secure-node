#https://tox.readthedocs.io/en/latest/ => convert to tox
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="p2psecure",
    version="0.0.1",
    author="Maurice Snoeren",
    author_email="macsnoeren@gmail.com",
    description="Python decentralized peer-to-peer secure network application framework based on p2pnetwork.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/macsnoeren/python-p2p-secure",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite='nose.collector',
    tests_require=['nose'],
)
