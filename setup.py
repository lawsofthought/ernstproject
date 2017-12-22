from setuptools import setup
import unittest

def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('ernst', pattern='_test*.py')
    return test_suite

setup(name = "ernst",
      license = 'GNU Public License 3.0',
      version = "0.0.0",
      description = "Miscellaneous",
      author = "Mark Andrews",
      author_email = "mjandrews.net@gmail.com",
      packages=["ernst"],
      test_suite='setup.test_suite',
)
