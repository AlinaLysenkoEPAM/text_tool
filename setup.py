from setuptools import setup, find_packages

setup(
    name='text_tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'text_tool=text_tool.main:main',
        ],
    },
    author='Alina Lysenko',
    author_email='Alina_Lysenko1@epam.com',
    description='A command-line tool to process text files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AlinaLysenkoEPAM/text_tool',
)
