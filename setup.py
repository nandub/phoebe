from setuptools import setup

setup(
    name='phoebe',
    version='2.1.2',
    author='Crisper Hills',
    author_email='jrh@example.com',
    packages=['phoebe'],
    scripts=['bin/phoebe_run', 'bin/phoebe_play'],
    url='http://pypi.python.org/pypi/phoebe',
    license='LICENSE',
    description='an adaptive, transcoding media robot for ICanHazChat',
    long_description=open('README.md').read(),
    install_requires=[
        "setuptools >= 41.2.0",
        "circuits >= 3.2",
        "lxml >= 4.5.0",
        "pyOpenSSL >= 19.1.0",
        "requests >= 2.23.0",
        "PyYAML >= 5.3.1",
        "setproctitle >= 1.1.10",
        "PyGObject >= 3.36.0",
    ],
)

