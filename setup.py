from setuptools import setup

setup(name="qmpy_rester",
      version='0.1',
      description="A python code to query OQMD data through oqmd-api",
      url="https://github.com/mohanliu/qmpy_rester",
      author="Mohan Liu",
      author_email="mohan@u.northwestern.edu",
      license="LICENSE",
      packages=['qmpy_rester'],
      long_description=open('README.md').read(),
      install_requires=[
          "requests",
          "json",
          ],
      )

    