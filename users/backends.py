from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()

# class EmailBackend(ModelBackend):
#     def authenticate(self,request,username=None,password=None,**kwargs):
#         try:
#             user = UserModel.objects.get(Q(username_iexact = username)| Q(email_iexact=username))
#         except UserModel.DoesNotExist:
#             #for newly created applicationt
#             UserModel().set_password(password)
#             return
#         except UserModel.MultipleObjectsReturned:
#             #prevent multiple obj return and filter first user of it
#             user = UserModel.objects.filter(Q(username_iexact = username)|Q(email_iexact = username)).order_by('id').first()
#         if user.check_password(password) and self.user_can_authenticate(user):
#             return user
        


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            # User does not exist
            return None
        except UserModel.MultipleObjectsReturned:
            # Prevent multiple objects returned and filter first user
            user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
