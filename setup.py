from setuptools import setup
from elasticsearchcli.utils import escli_version

setup(name='elasticsearchcli',
      version=escli_version,
      description='A command line utility to interact with Elasticsearch',
      url='https://github.com/hamzb/escli',
      author='Hamza Boulaares',
      author_email='hamza.boulaares@gmail.com',
      license='GPLv3.0',
      packages=['elasticsearchcli'],
      zip_safe=False,
      install_requires=['elasticsearch'],
      python_requires='>=3',
      scripts=['escli'],
      classifiers=["Programming Language :: Python :: 3"],
      )