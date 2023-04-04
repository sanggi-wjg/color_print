from setuptools import setup, find_packages

setup(
    name='colorful-print',
    version='0.1.0',
    url='https://github.com/sanggi-wjg/color_print',
    author='SangGi',
    author_email='girr311@naver.com',
    description='Can it be used to print in color.',
    packages=find_packages(exclude=['tests']),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[],
    zip_safe=False,
    project_urls={
        "Bug Tracker": "https://github.com/sanggi-wjg/color_print/issues",
    },
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ]
)
