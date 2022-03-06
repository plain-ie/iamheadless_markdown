from distutils.core import setup

setup(
    # Application name:
    name="iamheadless_markdown",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="Maris Erts",
    author_email="maris@plain.ie",

    # Packages
    packages=["iamheadless_markdown"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="#",

    #
    # license="LICENSE.txt",
    description="#",

    # long_description=open("README.md").read(),

    # Dependent packages (distributions)
    install_requires=[
        "Django==4.0.1",
    ],
)
