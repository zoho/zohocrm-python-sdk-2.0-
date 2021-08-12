from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zohocrmsdk2_0',
    version='2.0.1',
    description='Zoho CRM SDK for Python developers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zoho/zohocrm-python-sdk-2.0',
    author='Zoho CRM API Team',
    author_email='support@zohocrm.com',
    scripts=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'requests',
        'python-dateutil',
        'urllib3'
    ],
    keywords=['development', 'zoho', 'crm', 'api', 'zcrmsdk', 'sdk', 'zcrm','zohocrmsdk2_0'],
    packages=find_packages(),
    include_package_data=True
)
