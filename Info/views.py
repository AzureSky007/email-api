from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import User
from .serializers import UserSrlzr
from rest_framework import status

grt = ["Hello", "Hi", "Hola", "Bonjour", "Guten Tag", "Ciao", "Namaste", "Konnichiwa",
       "Salaam", "Shalom", "Merhaba", "Szia", "Hallo", "Aloha", "Selamat pagi", "Sawatdee",
       "Zdravstvuyte", "Dobrý den", "Hej", "Salam"]

def is_valid_email(email):
    return email.endswith("@gmail.com")

def is_valid_name(name):
    return name.isalpha()

def is_valid_city(city):
    return city.isalpha()

def get_next_attribute(user):
    if user.greet is None:
        return 'greet'
    elif user.email is None:
        return 'email'
    elif user.name is None:
        return 'name'
    elif user.city is None:
        return 'city'
    else:
        return None

def save_attribute(user, attribute, value):
    setattr(user, attribute, value)
    user.save()

class GreetingView(APIView):
    def get(self, request, num=None):
        user_obj = User.objects.all()
        user_srlzr = UserSrlzr(user_obj,many=True)
        return Response(user_srlzr.data,status = status.HTTP_200_OK)
    
    def post(self, request, num=None, value=None):
        if num is None:
            return Response({"msg": "Enter your number"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(num=num)
        except User.DoesNotExist:
            user = User.objects.create(num=num)
            return Response({"msg": "Hello there! User Created"}, status=status.HTTP_200_OK)

        attributes = ['greet', 'email', 'name', 'city']

        for attribute in attributes:
            if attribute == 'greet' and not user.greet:
                if value is not None:
                    user.greet = value
                    user.save()
                    return Response({"msg": "Value saved to greet attribute. Enter your email"}, status=status.HTTP_200_OK)
                else:
                    return Response({"msg": "Enter your greet"}, status=status.HTTP_200_OK)
            
            if attribute == 'email' and not user.email:
                if value is not None:
                    user.email = value
                    user.save()
                    return Response({"msg": "Value saved to email attribute. Enter your name"}, status=status.HTTP_200_OK)
                else:
                    return Response({"msg": "Enter your email"}, status=status.HTTP_200_OK)
            
            if attribute == 'name' and not user.name:
                if value is not None:
                    user.name = value
                    user.save()
                    return Response({"msg": "Value saved to name attribute. Enter your city"}, status=status.HTTP_200_OK)
                else:
                    return Response({"msg": "Enter your name"}, status=status.HTTP_200_OK)
            
            if attribute == 'city' and not user.city:
                if value is not None:
                    user.city = value
                    user.save()
                    send_mail(
                        subject='Subject',
                        message=f"""Hello {user.name}, your data was created.
                        \nThe email we've sent this one is {user.email}
                        \n The number you entered was {user.num} 
                        \n The city you entered was {user.city}""",
                        from_email='thememeluniacs@gmail.com',
                        recipient_list=[user.email],
                        fail_silently=False
                    )
                    return Response({"msg": "Value saved to city attribute and email sent"}, status=status.HTTP_200_OK)
                else:
                    return Response({"msg": "Enter your city"}, status=status.HTTP_200_OK)

        return Response({"msg": "All attributes are already filled"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format = None):
        user_obj = User.objects.all()
        user_obj.delete()
        return Response({'msg':'Data Deleted'})
    
    # def post(self, request, num=None, value=None):
    #     if num is None:
    #         return Response({"msg": "Enter your number"}, status=status.HTTP_400_BAD_REQUEST)
    #     try:
    #         user = User.objects.get(num=num)
    #     except User.DoesNotExist:
    #         user = User.objects.create(num=num)
    #         return Response({"msg": "Hello there! User Created"}, status=status.HTTP_200_OK)
                    
    #     if num is not None and value is not None:
    #         user.greet = value
    #         user.save()
            
    #         if num is not None and user.greet is not None:
    #             user.email = value
    #             user.save()
                
    #             if num is not None and user.email is not None:
    #                 user.name = value
    #                 user.save()
                    
    #                 if num is not None and user.name is not None:
    #                     user.city = value
    #                     user.save()
                            
    #                     send_mail(
    #                             subject='Subject',
    #                             message=f"""Hello {user.name}, your data was created.
    #                             \nThe email we've sent this one is {user.email}
    #                             \n The number you entered was {user.num} 
    #                             \n The city you entered was {user.city}""",
    #                             from_email='thememeluniacs@gmail.com',
    #                             recipient_list=[user.email],
    #                             fail_silently=False
    #                         )
    #                     return Response({"msg": "The mail has been sent!"})
    #                 else:
    #                     return Response({"msg": "Enter your city"}, status=status.HTTP_400_BAD_REQUEST)
    #             else:
    #                 return Response({"msg": "Enter your name"}, status=status.HTTP_400_BAD_REQUEST)
    #         else:
    #             return Response({"msg": "Enter your email"}, status=status.HTTP_400_BAD_REQUEST)    
    #     else:
    #         return Response({"msg": "Hello there! No value entered"}, status=status.HTTP_400_BAD_REQUEST)
                
                