from typing import Callable, List

def pre_process_text(text:str,functions:List[Callable]):
    for function in functions:
        text = function(text)
    return text


