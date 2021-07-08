from django.contrib.auth.models import User


class EmailAuthentication(object):
    def authenticate(self, request, username, password):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, id):
        try:
            return User.objects.filter(pk=id)
        except user.DoesNotExist:
            return None
