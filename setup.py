from setuptools import setup

setup(
    name='Unison',
    version='1.0.1-alpha',
    packages=['unison', 'unison.apis', 'unison.data', 'unison.tests',
              'unison.classes', 'unison.modules'],
    url='https://github.com/Kwistech/Unison',
    license='Open Software License 3.0',
    author='Johnathon Kwisses',
    author_email='johnkwisses@gmail.com',
    description='Unison is a voice command and response program that '
                'gives a user the ability to control their computer via '
                'voice commands.',
    include_package_data=True
)
