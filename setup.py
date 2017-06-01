from setuptools import setup

setup(name='striketracker',
      version='0.5.2',
      description='Command line interface to the Highwinds CDN',
      url='https://github.com/Highwinds/striketracker',
      author='Mark Cahill',
      author_email='support@highwinds.com',
      license='MIT',
      packages=['striketracker'],
      install_requires=['requests>=2.0.1', 'PyYAML>=3.10', 'future', 'mock'],
      scripts=['bin/striketracker'],
      test_suite='nose.collector',
      tests_require=['nose', 'responses', 'coverage', 'future'],
      zip_safe=False)
