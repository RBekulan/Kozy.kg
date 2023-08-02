from rest_framework import status
from rest_framework import mixins
from rest_framework.views import APIView
from product.serializers import *
from rest_framework import generics
from rest_framework.response import Response
from .models import *


class ProductList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class Favorites(APIView):
    favorites = Product.favorites
    if favorites:
        pass


# from rest_framework import viewsets
# from rest_framework.response import Response
# from .models import Favorite
# from .serializers import FavoriteSerializer
#
#
# class FavoriteViewSet(viewsets.ModelViewSet):
#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteSerializer
#
#     def post(self, request, *args, **kwargs):
#         favorite_item_id = request.data.get('favorite_item')
#         user = request.user
#
#         # Проверяем, не добавлен ли объект уже в избранное для данного пользователя
#         if not Favorite.objects.filter(user=user, favorite_item_id=favorite_item_id).exists():
#             Favorite.objects.create(user=user, favorite_item_id=favorite_item_id)
#             return Response({'message': 'Item added to favorites.'})
#         else:
#             return Response({'message': 'Item is already in favorites.'})
#
#     def destroy(self, request, *args, **kwargs):
#         favorite_item_id = self.get_object().favorite_item_id
#         user = request.user
#
#         try:
#             favorite = Favorite.objects.get(user=user, favorite_item_id=favorite_item_id)
#             favorite.delete()
#             return Response({'message': 'Item removed from favorites.'})
#         except Favorite.DoesNotExist:
#             return Response({'message': 'Item is not in favorites.'})
