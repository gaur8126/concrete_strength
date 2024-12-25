from setuptools import setup ,find_packages
from typing import List

HYPEN_DOT = '-e .'

def get_requirements(filepath:str)->List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)

    return requirements


setup(
    name='concrete_strength',
    version='0.0.1',
    author='Lokesh',
    author_email='gaurlokesh1211@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)