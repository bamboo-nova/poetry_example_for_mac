class myclass:
    
    def __init__(self) -> None:
        self.init_val = 10
    
    def __call__(self, input_val: int) -> str:
        if isinstance(input_val, int):
            return str(self.init_val + input_val)
        else:
            return "Error"
