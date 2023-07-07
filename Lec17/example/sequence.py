"""
Модуль для описания и конструирования объектов класса Sequence
Каждый объект - .......
Особенноси - ...
Замечания - .....
"""

class Sequence: 
    """
    ....
    """
    def __init__(self, input_message:str): 
        """
        ....
        """
        self.message = input_message 
        
    def find_max(self): 
        """ 
        Calc max length and return this value 
        """
        return len(max(self.message.split("р")))
    
if __name__ == "__main__":
    print("Здесь будут действия, которые выполняются ИСКЛЮЧИТЕЛЬНО при прямом запуска данного модуля!!!")