# un decorator debe de tomar una función y regresar otra función
import functools


user = {'username': 'jose', 'access_level': 'admin'}


def user_has_permission(func):
    @functools.wraps(func)  #Le especifica que se está ampliando la funcionalidad de func(), no reemplaza el nombre/doc
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()

    return secure_func


@user_has_permission
def my_function():
    return 'Password admin panel is 1234'


print(my_function())
print(my_function.__name__)
