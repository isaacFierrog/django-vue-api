from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.usuario.models import Usuario
from apps.usuario.api.serializers import UsuarioSerializer, UsuarioTokenSerializer


class UsuarioViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all() 
    
    
class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print(request.data)
        login_serializer = self.serializer_class(
            data=request.data,
            context = {'request': request}
        )
        
        
        
        if login_serializer.is_valid():
            print(login_serializer.validated_data)
            usuario = login_serializer.validated_data['user']
            if usuario.is_active:
                token, created = Token.objects.get_or_create(user=usuario)
                
                if created:
                    return Response({
                        'token': token.key,
                        'usuario': UsuarioTokenSerializer(usuario).data,
                        'message': 'Inicio de sesion exitoso'
                    }, status=status.HTTP_201_CREATED)
                else: 
                    # sesiones = Session.objects.filter(expire_date__gte=datetime.now())
                    
                    # if sesiones.exists():
                    #     for sesion in sesiones:
                    #         sesion_data = sesion.get_decoded()
                    #         if usuario.id == int(sesion_data.get('_auth_user_id')):
                    #             sesion.delete()
                    
                    # token.delete()
                    # token = Token.objects.create(user=usuario)
                    # return Response({
                    #     'token': token.key,
                    #     'usuario': UsuarioTokenSerializer(usuario).data,
                    #     'message': 'Inicio de sesion exitoso'
                    # }, status=status.HTTP_201_CREATED)
                    return Response({
                        'error': 'Ya se ha iniciado sesion con este usuario'
                    }, status=status.HTTP_409_CONFLICT)
            else:
                return Response({
                    'error': 'Este usuario no puede iniciar sesion'
                }, status=status.HTTP_401_UNAUTHORIZED)
            
        return Response({
            'error': 'Datos incorrectos'
        }, status=status.HTTP_400_BAD_REQUEST)
        
        
class Logout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            token = Token.objects.filter(
                key=request.data.get('token')
            ).first()
        
            print(token)
            
            if token:
                usuario = token.user
                sesiones = Session.objects.filter(expire_date__gte=datetime.now())
                
                if sesiones.exists():
                    for sesion in sesiones:
                        sesion_data = sesion.get_decoded()
                        if usuario.id == int(sesion_data.get('_auth_user_id')):
                            sesion.delete()
                
                token.delete()
                mensaje_sesion = 'Sesiones de usuario eliminadas'
                mensaje_token = 'Token eliminado'
                
                return Response({
                    'mensaje_sesion': mensaje_sesion,
                    'mensaje_token': mensaje_token
                }, status=status.HTTP_200_OK)
            
            return Response({
                'error': 'No se ha encontrado un usuario con estas credenciales'
            }, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({
                'error': 'No se ha encontrado token en la peticion'
            }, status=status.HTTP_409_CONFLICT)