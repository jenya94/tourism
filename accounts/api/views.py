from django.contrib.auth import authenticate
from django.http.response import HttpResponse as Response
from rest_framework.authtoken.models import Token


class LoginView(APIView):
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)