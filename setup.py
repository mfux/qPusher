"""Package configuration."""
from setuptools import setup

setup(
    name="qPusher",
    version="0.1",
    packages=["qPusher"],
    package_dir={"": "src"},
    install_requires=["pytest==7.1.3", "black==22.10.0", "pytz"],
)
