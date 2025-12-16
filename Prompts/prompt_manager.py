from dataclasses import dataclass
import yaml
from typing import Dict
from os import path

class PromptNotLoaded(Exception):
    def __init__(self,message):
        super().__init__("prompt not loaded use method load_prompt() first")
@dataclass
class Prompt:
    """class for native prompts"""
    prompt_name : str
    prompt_version: int

class Prompt_Manager():
    def __init__(self,base_dir:str):
        self.base_dir : str = base_dir
        self.current_prompt_dict : Dict[str,str] = None
        self.current_prompt : Prompt = None 
    
    def load_prompt(self,prompt:Prompt):
        self.current_prompt = prompt
        print(path.join(self.base_dir,prompt.prompt_name,prompt.prompt_version + '.yaml'))
        with open(path.join(self.base_dir,prompt.prompt_name,prompt.prompt_version + '.yaml')) as f:
            self.prompt_dict = yaml.safe_load(f)
        print(self.current_prompt_dict)
    
    def build_prompt_message(self,insertions: Dict[str,str]):
        if not self.current_prompt:
            raise PromptNotLoaded
        
        

        


        pass
