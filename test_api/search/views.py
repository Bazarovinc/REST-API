from django.shortcuts import render
from django.db.models import Q
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer, SearchUsersSerializer


class UserView(APIView):

    def get(self, request, pk=0):
        if pk != 0:
            user = get_object_or_404(User.objects.all(), pk=pk)
            serializer = UserSerializer(user)
            return Response({'user': serializer.data})
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response({'users': serializer.data})

    def post(self, request):
        user = request.data.get('user')
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"succes": f"User {user_saved.name} created"})

    def put(self, request, pk):
        saved_user = get_object_or_404(User.objects.all(), pk=pk)
        data = request.data.get('user')
        serializer = UserSerializer(instance=saved_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": f"User '{user_saved.name}' updated successfully"})

    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(User.objects.all(), pk=pk)
        article.delete()
        return Response({"message": f"User with id {pk} has been deleted."}, status=204)


class SearchUserView(APIView):

    def get(self, request):
        search = request.data.get('search')
        serializer = SearchUsersSerializer(data=search)
        if serializer.is_valid(raise_exception=True):
            searching = serializer.data
            users = User.objects.filter(x__lte=(searching["x"] + searching["m"]),
                                        y__lte=(searching['y'] + searching["m"]))
            serializer_users = UserSerializer(users, many=True)
            return Response({'users': serializer_users.data[:searching["k"]]})

