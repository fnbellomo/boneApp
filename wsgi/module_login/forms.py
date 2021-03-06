from flask_wtf import Form 
from wtforms import TextField, PasswordField, BooleanField, SubmitField, validators

from models import DatosUsuarios


class MyForm(Form):
    username = TextField("Username", [validators.Required("Please enter your username.")])
    password = PasswordField("Password", [validators.Required("Please enter your password.")])
    remember_me = BooleanField('remember_me', default = False)
    submit = SubmitField("Sign In")

    def validate(self):

        datos = DatosUsuarios()
        Usuarios = datos.usuarios()
        Password = datos.password()
        
        rv = Form.validate(self)
        if not rv:
            return False

        if self.username.data in Usuarios:
            num_usuario = Usuarios.index(self.username.data)
        else:
            self.username.errors.append('Nombre de usuario invalido')
            return False

        if self.password.data != Password[num_usuario]:
            self.password.errors.append('Password Incorrecto')
            return False
             
        return True

        
SECRET_KEY = 'secret'

