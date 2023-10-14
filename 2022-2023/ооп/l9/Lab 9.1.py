class CustomButton():
    def __init__(self, text, **kwargs):
        self.text = text
        if kwargs:
            self.config(**kwargs)

    def config(self, **kwargs):
        for args_name in kwargs.keys():
            setattr(self, args_name, kwargs[args_name])

    def click(self):
        try:
            self.command()
        except AttributeError:
            print("Кнопка не настроена")

def func(): 
    print('Готово') 
 
btn = CustomButton(text="Hello", bd=20, bg='#ffaaaa') 
btn.click()  # Кнопка не настроена 
btn.config(command=func) 
btn.click()  # Готово