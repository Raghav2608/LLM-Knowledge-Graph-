from dataclasses import dataclass
import yaml
from typing import Dict
from os import path
@dataclass
class Prompt:
    """class for native prompts"""
    prompt_name : str
    prompt_version: int

class Prompt_Manager():
    def __init__(self,base_dir:str):
        self.base_dir : str = base_dir
        self.prompt_dict : Dict[str,str] = None
    
    def load_prompt(self,prompt:Prompt):
        self.current_prompt_template = prompt
        with open(path.join(self.base_dir,prompt.prompt_name,prompt.prompt_version + '.yaml')) as f:
            self.prompt_dict = yaml.safe_load(f)
    
    def build_prompt_message(self,insertions: Dict[str,str]):
        


        pass
