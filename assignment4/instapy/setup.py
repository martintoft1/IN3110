import setuptools
setuptools.setup(
    name="instapy",
    version="1.0",
    author="Martin Toft",
    packages=setuptools.find_packages(),
    scripts=["bin/instapy"],
    setup_requires=["numpy", "setuptools>=18.0"],
    install_requires=["numpy", "numba", "opencv-python"],
)