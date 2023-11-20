from setuptools import setup, find_packages

setup(
    name='faker-blog-provider',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'faker',
    ],
    author='Adaías Magdiel',
    author_email='adaiasmagdiell@gmail.com',
    description='Python faker blog content provider in Brazilian Portuguese',
    long_description=
    'Generate fictional blog data for your projects such as titles, tags, images, and much more.',
    long_description_content_type='text/markdown',
    url='https://github.com/AdaiasMagdiel/python-faker-blog',
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
