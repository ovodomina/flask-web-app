from setuptools import setup, find_packages

setup(
    name='flask-web-app',
    version='1.0.0',
    description='A simple Flask web application',
    author='Seu Nome',
    author_email='seuemail@example.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==3.0.3',
        'Werkzeug==3.0.4',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
