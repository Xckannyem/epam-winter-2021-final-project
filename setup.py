from setuptools import setup

setup(
    name='department_app',
    version='1.0',
    long_description=__doc__,
    author='Yehor Kolodii',
    author_email='yegorkolodii@gmail.com',
    packages=[
        'Flask>=1.1.2'
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)