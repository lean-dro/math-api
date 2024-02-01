class ResultResponse:
    def __init__(self, numbers: list, result: float):
        self.data:dict = {
            "numbers":numbers, 
            "result":result
        }
        