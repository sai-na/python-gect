class MyError(Exception):
    def __init__(self,value ,limit : int):
        self.value=value
        self.limit=limit
    def __str__(self):
        return(repr(f'{self.value} +  {self.limit}'))


try:
    raise MyError(3*2 , limit=2)
except MyError as e:
    print(e)