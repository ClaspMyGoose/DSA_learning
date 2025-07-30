

class BrowserHistory:

    def __init__(self, homepage: str):
        self.forwardstack = []
        self.backwardstack = []
        self.current = homepage 
        

    def visit(self, url: str) -> None:
        self.backwardstack.append(self.current)
        self.current = url 
        self.forwardstack = []

    def back(self, steps: int) -> str:
        
        if not self.backwardstack:
            return self.current
        
        possible_steps = len(self.backwardstack)

        if steps > possible_steps:
            steps = possible_steps 

        for i in range(steps):
            self.forwardstack.append(self.current)
            self.current = self.backwardstack.pop()

        return self.current 


    def forward(self, steps: int) -> str:

        if not self.forwardstack:
            return self.current 
        
        possible_steps = len(self.forwardstack)

        if steps > possible_steps:
            steps = possible_steps 
        
        for i in range(steps):
            self.backwardstack.append(self.current)
            self.current = self.forwardstack.pop()

        return self.current 


obj = BrowserHistory("zav.com")
obj.visit("kni.com")
param_2 = obj.back(7)
param_2 = obj.back(7)
param_3 = obj.forward(5)
param_3 = obj.forward(1)
obj.visit("pwrrbnw.com")
obj.visit("mosohif.com")
param_2 = obj.back(9)
