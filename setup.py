import setuptools


with open('requirements.txt', 'r') as file:
    install_requires = file.read().splitlines()


setuptools.setup(name='password_generator',
                 packages=['generator'],
                 install_requires=install_requires)
