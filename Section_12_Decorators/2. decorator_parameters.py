# un decorator debe de tomar una función y regresar otra función
import functools


user = {'username': 'jose', 'access_level': 'admin'}


def user_has_permission(func):
    @functools.wraps(func)  #Le especifica que se está ampliando la funcionalidad de func(), no reemplaza el nombre/doc
    def secure_func(panel):
        if user.get('access_level') == 'admin':
            return func(panel)

    return secure_func


@user_has_permission
def my_function(panel):
    return f'Password admin {panel} panel is 1234'


print(my_function('movies'))
print(my_function.__name__)
