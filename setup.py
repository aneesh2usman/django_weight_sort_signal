from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'License :: OSI Approved :: MIT License',
  "Environment :: Web Environment",
  "Framework :: Django",
  "Framework :: Django :: 2.0",
  "Framework :: Django :: 2.1",
  "Framework :: Django :: 2.1",
  "Intended Audience :: Developers",
  "Operating System :: OS Independent",
  "Programming Language :: Python",
  "Programming Language :: Python",
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3 :: Only",
  "Programming Language :: Python :: 3.6",
  "Programming Language :: Python :: 3.7",
  "Programming Language :: Python :: 3.8",
  "Topic :: Software Development :: Libraries :: Python Modules",
]
 
setup(
  name='django-weight-sort-signal',
  version='0.0.2',
  description='django signal sorting on weight via Django 2.*',
  # long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description=open('README.rst').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/aneesh2usman/django_weight_signal',  
  author='aneesh usman',
  author_email='aneeshplusone@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  include_package_data=True,
  keywords='Signal signal sorting receiver', 
  packages=find_packages(),
  python_requires=">=3.6",
  install_requires=[''] 
)
