from django.shortcuts import render
from django.db.models import Q
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer, SearchUsersSerializer
import sqlite3


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
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"succes": f"User {user_saved.name} created"}, status=201)

    def put(self, request, pk):
        saved_user = get_object_or_404(User.objects.all(), pk=pk)
        serializer = UserSerializer(instance=saved_user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": f"User '{user_saved.name}' updated successfully"})

    def delete(self, request, pk):
        # Get object with this pk
        user = get_object_or_404(User.objects.all(), pk=pk)
        user.delete()
        return Response({"message": f"User with id {pk} has been deleted."}, status=204)


class SearchUserView(APIView):

    def get(self, request):
        serializer = SearchUsersSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            searching = serializer.data
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.cursor()
            cur.execute("SELECT * FROM search_user WHERE"
                        f"(x <= ({searching['x']} + {searching['m']}) AND y <= ({searching['y']} + {searching['m']}))"
                        "AND"
                        f"(x >= ({searching['x']} - {searching['m']}) AND y <= ({searching['y']} + {searching['m']}))"
                        "AND"
                        f"(x >= ({searching['x']} - {searching['m']}) AND y >= ({searching['y']} - {searching['m']}))"
                        "AND"
                        f"(x <= ({searching['x']} + {searching['m']}) AND y >= ({searching['y']} - {searching['m']}))"
                        "ORDER BY x, y")
            users_bad_type = cur.fetchall()
            conn.commit()
            users = []
            if len(users_bad_type) != 0:
                for user in users_bad_type[:searching['k']]:
                    d = {"id": user[0], "name": user[1], "x": user[2], "y": user[3], "description": user[4]}
                    users.append(d)
                return Response({'users': users})
            else:
                return Response({'message': "No one user was found."}, status=200)

