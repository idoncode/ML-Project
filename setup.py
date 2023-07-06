from setuptools import find_packages, setup
from typing import List


hyphen_e_dot = '-e .'
def get_requirements(file_name:str) -> List[str]:
    '''
    This function will return the list of elements
    '''
    requirements = []
    with open(file_name) as f:
        requirements = f.readlines()
        requirements = [i.replace('\n', '') for i in requirements]

    if hyphen_e_dot in requirements:
        requirements.remove(hyphen_e_dot)


setup(
    name = 'ML-Project',
    version = '0.0.1',
    author = 'Soham',
    author_email='girisoham84@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)