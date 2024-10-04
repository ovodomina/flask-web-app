from setuptools import setup, find_packages

setup(
    name='flask-web-app',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'flask-web-app = app:app.run',
        ],
    },
)
