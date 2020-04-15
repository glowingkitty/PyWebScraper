import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyWebScraper",  # Replace with your own username
    version="0.0.5",
    author="Marco",
    author_email=None,
    description="A web scraper that combines both Beautiful Soup (bs4) and Selenium.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcoEDU/PyWebScraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'bs4',
        'requests',
        'selenium'
    ]
)
