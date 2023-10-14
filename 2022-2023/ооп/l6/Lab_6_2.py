class Addition:
    def __call__(self, *args, **kwargs):
        args_summ = 0
        
        for i in args:
            if isinstance(i, (int, float)):
                args_summ += i
        
        print(args_summ)


add = Addition() 
add(10, 20) # печатает "Сумма переданных значений = 30" 
add(1, 2, 3.4) # печатает "Сумма переданных значений = 6.4" 
add(1, 2, 'hello', [1, 2], 3) # печатает "Сумма переданных значений = 6"