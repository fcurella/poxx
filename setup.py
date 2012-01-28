from setuptools import setup, find_packages


version = (1, 0, 0)

install_requires = [
    'polib',
]

setup(
    name='poxx',
    version='1.0',
    author='Ned Batchelder, Package by Jacob Burch',
    author_email='jacobburch@revsys.com',
    url='http://github.com/jacobb/poxx',
    description='Faked translations',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    license='BSD',
    include_package_data=True,
    scripts=['poxx.py'],
    classifiers=[
        'Intended Audience :: Developers',
    ],
)