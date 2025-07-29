from setuptools import setup, find_packages

setup(
    name="EthicalHawk",
    version="1.0.0",
    description="Advanced Ethical Hacking, Pentesting & Bug Bounty Toolkit with AI Agent",
    author="HighKali",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "PyYAML",
        "torpy",
        "stem",
        "tweepy",
        "shodan",
        "censys",
        "wappalyzer"
    ],
    entry_points={
        'console_scripts': [
            'ethicalhawk=ethicalhawk:main',
        ],
    },
    include_package_data=True,
)