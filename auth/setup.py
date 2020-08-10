from setuptools import setup
from setuptools import find_packages


setup(
    name="auth",
    version="1.0.0",
    # packages=["auth"],
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