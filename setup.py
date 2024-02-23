from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name='cli-jarvis',
    version='0.0.1',
    author='Aarsh Shah',
    author_email='aarsh@live.ca',
    license='MIT License',
    description='This is a personalized assistance: Jarvis',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/AarshShah9/Jarvis-CLI',
    py_modules=['jarvis', 'app'],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        jarvis=jarvis:cli
    '''
)
