from setuptools import setup

setup(name='elasticsearchcli',
      version='0.1-alpha',
      description='A command line utility to interact with Elasticsearch',
      url='https://github.com/hamzb/escli',
      author='Hamza Boulaares',
      author_email='hamza.boulaares@gmail.com',
      license='GPLv3.0',
      packages=['elasticsearchcli'],
      zip_safe=False,
      install_requires=[
          'elasticsearch',
          'argparse'
      ],
      scripts=['bin/escli'])