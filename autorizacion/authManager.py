from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
    def created_user(self, correo, nombre, rol, password):
        if not  correo:
            raise ValueError('El usuario debe tener obligatoriamemnte un coprreo')
        correo = self.normalize_email(correo)
        nuevoUsuario=self.model(correo= correo, nombre= nombre, rol= rol)
        nuevoUsuario.set_password(password)

        nuevoUsuario.save(using=self._db)
        return nuevoUsuario
        
    def create_superuser(self, correo, nombre, rol, password):
        usuario = self.created_user(correo, nombre, rol, password)
        usuario.is_superuser=True
        usuario.is_staff=True

        usuario.save(using=self._db)

