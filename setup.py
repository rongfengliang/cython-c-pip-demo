import setuptools
from distutils.extension import Extension
from Cython.Build import cythonize
with open("README.md", "r") as fh:
    long_description = fh.read()

add_extension = Extension(
    name="add_app",
    sources=["./cli/app.pyx"],
    libraries=["add"],
    library_dirs=["ext"],
    include_dirs=["ext"]
)

setuptools.setup(
    name="dalongrong_cythoncli",
    version="0.0.4",
    author="dalongrong",
    author_email="1141591465@qq.com",
    description="a simple cli project",
    long_description=long_description,
    install_requires=['click'],
    ext_modules= cythonize([add_extension]),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Documentation': 'https://github.com/rongfengliang/click-cli-demo.git',
        'Say Thanks!': 'https://github.com/rongfengliang/click-cli-demo.git',
        'Source': 'https://github.com/rongfengliang/click-cli-demo.git',
        'Tracker': 'https://github.com/rongfengliang/click-cli-demo.git',
    },
    entry_points={
        'console_scripts': [
            'podcli=cli:apply',
        ],
    }
)