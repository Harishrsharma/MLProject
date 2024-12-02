from setuptools import find_packages, setup
from typing import List


# def get_requirements(file_path: str) -> List[str]:
#     '''
#     This function will retuen list of requirement
#     '''
#     requirements= []
#     with open(file_path) as file_obj:
#         requirements = file_obj.readline
#         requirements = [req.replace('\n',"") for req in requirements]

#     return requirements

def get_requirements(file_path):
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    # Remove any empty lines or newline characters
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    return requirements




setup(
name='mlproject',
version='0.0.1',
author='Harish_Sharma',
author_email='harishrsharma1405@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)