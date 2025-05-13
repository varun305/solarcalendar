from setuptools import setup, find_packages

setup(
    name="solarcalendar",
    version="0.1.0",
    author="Name",
    description="Calendars for the solar system",
    packages=find_packages(exclude=["tests*"]),
    python_requires=">=3.7",
    install_requires=[],
)
