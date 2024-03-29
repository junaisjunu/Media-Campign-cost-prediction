from setuptools import find_packages,setup
from typing import List



setup(
    name='Media_campign_cost_prediction',
    version='0.0.1',
    author='Junais',
    author_email='junaisk456@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)