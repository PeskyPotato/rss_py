from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='rss_py',
    version='0.2.0',
    description='Write an RSS feed',
    long_description=readme(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
    ],
    url='https://github.com/peskypotato/rss_py',
    author='PeskyPotato',
    license='MIT',
    packages=['rss_py'],
    install_requires=[
        'Jinja2'
    ],
    zip_safe=False,
    include_package_data=True)