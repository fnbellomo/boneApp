"Este script es para saber que usuarios tengo definido"
"seria mi ""base de datos"" jaja"

class DatosUsuarios():
  def leer_datos(self):

    archivo = open("wsgi/module_login/usuarios", "r")
    
    self.list_usuarios = []
    self.list_password = []
    self.list_permisos = []

    for line in archivo.readlines():
      (usuario, password, root, email) = line.split(",")
      self.list_usuarios.append(usuario)
      self.list_password.append(password)
      self.list_permisos.append(root)

    archivo.close()

  def usuarios(self):
    self.leer_datos()
    return self.list_usuarios

  def password(self):
    self.leer_datos()
    return self.list_password

  def permisos(self):
    self.leer_datos()
    return self.list_permisos
