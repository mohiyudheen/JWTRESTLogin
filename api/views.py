
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializer
    
class Login(TokenObtainPairView):
    '''
    Login Api Using JWT
    '''
    serializer_class = serializer.LoginSerializer
    token_obtain_pair = TokenObtainPairView.as_view()