import re
from uuid import RESERVED_FUTURE
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request

class SoloAdminPuedeEscribir(BasePermission):
    def has_permission(self, request: Request, view):


        print(request.user)
        print(request.user.nombre)
        print(request.user.rol)
        print(request.auth)
        print(request.method)
        print(SAFE_METHODS)
        print(type(view))



        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.rol == 'ADMINISTRADOR'

        return True if request.method in SAFE_METHODS else request.user.rol == 'ADMINISTRADOR'

       

        # return request.user.rol == 'ADMINISTRADOR'


        # if request.user.rol == 'ADMINISTRADOR':
        #     return True
        # else:
        #     return False
        #return True
        #return super().has_permission(request, view)

class SoloMozoPuedeEscribir(BasePermission):
    def has_permission(self, request, view):
        if request.method == SAFE_METHODS:
            return True
        else:
            return request.user.rol == 'MOZO'
