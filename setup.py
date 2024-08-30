from setuptools import find_packages, setup

setup(
    name='scverse-workshop',
    version='0.1',
    packages=find_packages(),
    install_requires=open('requirements.txt').read(),
    entry_points={
        'console_scripts': [
            'scverse=scverse.cli.main:main',
        ],
    },
)
