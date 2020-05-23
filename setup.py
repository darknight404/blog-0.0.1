from setuptools import find_packages, setup

setup(
    name="blog",
    version="0.0.1",
    description="Blog constructed from miguelgrinberg.com ",
    author="darknight404",
    author_email="josephgerald404@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    extras_require={"env": ["python-dotenv"]},
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
)
