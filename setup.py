from setuptools import setup, find_packages

setup(
    name = 'ColorPrint',
    version = '0.0.1',
    url = 'https://github.com/sanggi-wjg/color_print.git',
    author = 'SangGi',
    author_email = 'girr311@naver.com',
    description = 'Can use it to color print.',
    packages = find_packages(exclude = ['tests']),
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    install_requires = ['requirements'],
    zip_safe = False,
    classifiers = [
        'License :: OSI Approved :: MIT License'
    ]
)
