class RunTimeErrorWithCode(TypeError):
    """
    Exeption when an specific code is needed
    """
    def __init__(self,message,code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

#raise RunTimeErrorWithCode('An error has ocurred',500)
err = RunTimeErrorWithCode('An error has ocurred',500)
print(err.__doc__)