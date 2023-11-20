from setuptools import setup, find_packages
from pathlib import Path

README = Path(__file__).joinpath('README.md').read_text()
VERSION = Path(__file__).joinpath('faker_blog/VERSION').read_text()

setup(
    name='faker-blog-provider',
    version=VERSION,
    packages=find_packages(exclude=["tests", "build"]),
    install_requires=[
        'faker',
    ],
    author='Adaías Magdiel',
    author_email='adaiasmagdiell@gmail.com',
    description=
    'Generate fictional blog data for your projects such as titles, tags, images, and much more.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/AdaiasMagdiel/python-faker-blog',
    license="MIT",
    license_files=["LICENSE"],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Natural Language :: Portuguese (Brazilian)', 'Topic :: Utilities'
    ],
    keywords="faker blog portuguese fake-data article python mocking",
    python_requires='>=3'
)
