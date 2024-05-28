from django.shortcuts import render
from books.models import Book
from books.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics,viewsets
from books.serializers import UserSerializer
from django.contrib.auth.models import User
# Create your views here.
# class BookList(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BookList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)


# class BookDetail(APIView):
#     def get_object(self,request,pk):
#         try:
#             book = Book.objects.get(pk=pk)
#         except:
#             raise Http404
#
#     def get(self,request,pk):
#         book=self.get_object(request,pk)
#         b = BookSerializer(book)  # converts into json
#         return Response(b.data)    #sends json data to client
#     def put(self,request,pk):
#         book=self.get_object(request,pk)
#         b = BookSerializer(book, data=request.data)  # converts json data send from client to django format
#         if(b.is_valid()):
#             b.save()    #save record into database table
#             return Response(b.data,status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         book=self.get_object(request,pk)
#         book.delete()  # deletes from table
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class BookDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer
#
#
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
#

# class BookList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetails(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class user_logout(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


