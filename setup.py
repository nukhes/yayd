from setuptools import setup, find_packages

setup(
    name='yayd',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'yt-dlp',
    ],
    entry_points={
        'console_scripts': [
            'yayd=yayd.downloader:main',
        ],
    },
    author='nukhes',
    author_email='nukhes@protonmail.com',
    description='Easy YouTube downloader built with yt-dlp.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nukhes/yayd',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
