from setuptools import setup, find_packages

setup(
    name = 'colorful-print',
    version = '0.0.6',
    url = 'https://github.com/sanggi-wjg/color_print.git',
    author = 'SangGi',
    author_email = 'girr311@naver.com',
    description = 'Can use it to color print.',
    packages = find_packages(exclude = ['tests']),
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    install_requires = [],
    zip_safe = False,
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ]
)
