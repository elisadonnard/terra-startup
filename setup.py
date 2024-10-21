from setuptools import setup


setup(name='terra_init',
      version='0.0.1',
      description='setup terra imports',
      author='Ray Jones',
      author_email='thouis@gmail.com',
      packages=['terra_init'],
      install_requires=["pandas",
                        "tqdm",
                        "scanpy",
                        "seaborn",
                        "scipy",
                        "terra_pandas"],
      )
