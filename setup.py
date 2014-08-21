from setuptools import setup
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'hellosign_sdk'))

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='hellosign-python-sdk',
      version='3.2',
      description="A Python wrapper for the HelloSign API (http://www.hellosign.com/api)",
      long_description=readme(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='hellosign python sdk',
      url='https://github.com/HelloFax/hellosign-python-sdk',
      author='HelloSign',
      author_email='apisupport@hellosign.com',
      license='MIT',
      packages=[
        'hellosign_sdk',
        'hellosign_sdk.utils',
        'hellosign_sdk.resource',
        ],
      install_requires=[
        'requests'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
