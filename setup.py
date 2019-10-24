from distutils.core import setup
import sys

packages = \
['nparser']

package_data = \
{'': ['*']}

install_requires = []
if sys.version_info[0] < 3 and sys.version_info[1] < 7:
    install_requires = ['dataclasses']

extras_require = \
{'dev': ['black'], 'test': ['pytest', 'pytest-raises']}

setup(name='nparser',
      version='0.1.1',
      description='Nginx error log parser.',
      author='Jin Nguyen',
      author_email='dangtrinhnt@mymusictaste.com',
      url='https://github.com/MyMusicTaste/nparser',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      extras_require=extras_require,
      python_requires='',
     )
