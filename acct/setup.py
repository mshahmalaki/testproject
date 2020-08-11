from setuptools import setup
from setuptools import find_packages


setup(
    name="acct",
    version="1.0.0",
    # packages=["acct"],
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "black",
        "coverage",
        "cryptography",
        "flake8",
        "isort",
        "flask",
        "flask-sqlalchemy",
        "flask-migrate",
        "flask-marshmallow",
        "flask-restx",
        "flask-jwt-extended",
        "marshmallow-sqlalchemy",
        "pymysql",
        "pymysql[rsa]",
        "pytest",
        "python-dotenv",
        "requests",
        "simplejson",
        "gunicorn"
    ]
)
from setuptools import find_packages


