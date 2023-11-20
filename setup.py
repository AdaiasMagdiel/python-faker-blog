from setuptools import setup, find_packages
from pathlib import Path


def read(*names, **kwargs):
    file_path = Path(__file__).resolve().parent.joinpath(*names)
    encoding = kwargs.get("encoding", "utf-8")

    return file_path.read_text(encoding=encoding).strip()


setup(
    name='faker_blog_provider',
    version='1.0.6',
    packages=find_packages(exclude=["tests", "build"]),
    author='Adaías Magdiel',
    author_email='adaiasmagdiell@gmail.com',
    description=
    'Generate fictional blog data for your projects such as titles, tags, images, and much more.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/AdaiasMagdiel/python-faker-blog',
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
    python_requires='>=3',
    setup_requires=['wheel']
)
