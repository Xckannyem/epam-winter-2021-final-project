from setuptools import setup, find_packages

setup(
    name='department_app',
    version='1.0',
    long_description=__doc__,
    author='Yehor Kolodii',
    author_email='yegorkolodii@gmail.com',
    url='https://gitlab.com/yehor.k/epam-winter-2021-final-project',
    install_requires=[
        'Flask>=1.1.2',
        'Flask-Migrate>=2.7.0',
        'Flask-SQLAlchemy>=2.5.1',
        'Flask-RESTful>=0.3.8'
        'psycopg2-binary==2.8.6'
    ],
    include_package_data=True,
    zip_safe=False,
    packages=find_packages()
)
