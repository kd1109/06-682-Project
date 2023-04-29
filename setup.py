"""
Setup script for pkg package.
"""

from setuptools import setup

setup(name='06-682-Project',
      version='0.0.1',
      
      description='bibtex and ris utilities',
      maintainer='Kathan',
      maintainer_email='kathanjd@andrew.cmu.edu',
      license='MIT',
      packages=['openalex'],
      scripts=[],
      entry_points={
        "console_scripts": ["cite = openalex.cmdline:cite"]},
      long_description='''to get citations bibtex/ris''')
