import setuptools

setuptools.setup(
    name="demo_reader_plural",
    version="1.0.0",
    description="Tools for reading various file formats",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'}
    )