from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework import status
from watchlist_app.models import Movie
from .serializers import MovieSerializer

class MovieListAv(APIView):
    
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class MovieDetailAv (APIView):
    def get(self, request, pk):
        if request.method == 'GET':
            try:            
                movie = Movie.objects.get(pk=pk)
            except Movie.DoesNotExist:
                return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        
    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
           

    
        


"""Using Function based view"""
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':        
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:            
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         else:
#             return Response(serializer.errors)
        
    
#     elif request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete
#         return Response(status=status.HTTP_204_NO_CONTENT)