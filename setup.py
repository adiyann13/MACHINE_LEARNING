from setuptools import find_packages ,setup
from typing import List

requirements = []
def get_reuirements(file_nameh:str)->List[str]:
    
    with open(file_nameh) as fn:
        requirements = fn.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        return requirements
        
stup = setup(
    name = "machine_learning_proj",
    version = '1.0',
    author = 'ádiyan',
    packages=find_packages(),
    requires = get_reuirements('requirements.txt')
)