from setuptools import setup, find_packages


setup(
    name='pyjones',
    version='0.1.0',
    description='A package for calculating light polarizations',
    author='Nicolas Tolazzi',
    author_email='nicolas.tolazzi@googlemail.com',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['numpy'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3']
)
