# python --version
# virtualenv env
# .\env\Scripts\activate
# .\env\Scripts\deactivate
# pip install django
# django-admin startproject danjoApp
# python manage.py runserver
# python manage.py shell

# django views are responsible for rendering html template

# django rest framework ---> views that convert python function into api view function
# so this functions are capable of handling all api related things

# from rest_framework.decorators import api_view
# api_view decorator

# @api_view(['GET', 'POST', 'PATCH'])
# def post(request):
#     courses = {
#         'course_name': 'python',
#         'course_provider': 'scaler'
#     }
#     if request.method == 'GET':
#         objs = Person.objects.all()
#         serializer = PersonSerializer(objs, many=True)
#         # return Response(serializer.data)
#         print("get method")
#         return Response(courses)
#     elif request.method == 'POST':
#         data = request.data
#         serializer = PersonSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             # return Response(serializer.data)
#         # return Response(serializer.errors)
#         print("post method")
#         return Response(courses)
#     else:
#         data = request.data
#         obj = Person.objects.get(id=data['id'])
#         # obj.delete()
#         serializer = PersonSerializer(obj, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             # return Response(serializer.data)
#         # return Response(serializer.errors)
#         print("post method")
#         return Response(courses)


# Model Person
# Person.objects.all() --> type = queryset
# To expose this queryset to frontend we need json format and that is done by serializer
# Also if we want to save data that comes in json format in post request in
# queryset form we use serializer

# class Person(models.Model):
#     color_field = models.ForeignKey(Color,on_delete=models.CASCADE,related_name = "color_field")
#     Color is another model
#     name= models.CharField(max_length=100)
#     age = models.IntegerField()


# class PersonSerializer(serializer.ModelSerializer):
#     class Meta:
#         model = Person
#         fields = ['name', 'age']
#         # depth = 1 --> upto 1st nested model

#     def validate_age(self, age):
#         if age < 18:
#             raise serializer.ValidationError('age should be greater than 18')
#         return age

#     def validate(self, data):
#         if data['age'] > 60:
#             raise serializer.ValidationError('age should be lesser than 60')
#         return data


# ApiView is a class
# class Person(APIView):
#     def get(self, request):
#         return Response({'message': 'get method'})

#     def post(self, request):
#         return Response({'message': 'post method'})

#     def patch(self, request):
#         return Response({'message': 'patch method'})


# Person.as_view()
# User.objects.filter(username=data['username']).exists()
# request.user
# permission_classes
# authenciation_classes
