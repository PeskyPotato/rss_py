from setuptools import setup

setup(name='rss_py',
      version='0.1',
      description='Write an RSS feed',
      url='https://github.com/peskypotato/rss_py',
      author='PeskyPotato',
      license='MIT',
      packages=['rss_py'],
      install_packages=[
          'Jinja2'
      ],
      zip_safe=False,
      include_package_data=True)