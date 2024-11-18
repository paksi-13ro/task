def test_function():
    def inner_function(x):
        print("Я в области видимости функции test_function")

    inner_function()


inner_function()
