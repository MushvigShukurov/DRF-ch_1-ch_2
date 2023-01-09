from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import generics
from kitablar.api.serializers import KitabSerializer, YorumSerializer
from kitablar.models import Kitab, Yorum
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from kitablar.api.pagination import SmallPagination, LargePagination
from kitablar.api.permissions import IsAdminUserOrReadOnly, IsYorumSahibiOrReadOnly
from rest_framework.exceptions import ValidationError

class KitabListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitab.objects.all().order_by('-id')
    serializer_class = KitabSerializer
    # permission_classes = [permissions.IsAdminUser]
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallPagination


class KitabDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitab.objects.all()
    serializer_class = KitabSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class YorumCreateAPIView(generics.CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        kitab_pk = self.kwargs.get("kitab_pk")
        kitab = get_object_or_404(Kitab,pk=kitab_pk)
        kullanici = self.request.user
        yorumlar = Yorum.objects.filter(kitab=kitab,yorum_sahibi=kullanici)
        if yorumlar.exists():
            raise ValidationError("Bir kitaba yalnız bir şərh yaza bilərsiniz.")
        serializer.save(kitab=kitab,yorum_sahibi=kullanici)


class YorumDetaulAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsYorumSahibiOrReadOnly]

   


# class KitabListCreateAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):

#     queryset = Kitab.objects.all()
#     serializer_class = KitabSerializer

#     # Listle
#     def get(self,request, *args, **kvargs):
#         return self.list(request, *args, **kvargs)

#     # Yarat
#     def post(self,request, *args, **kvargs):
#         return self.create(request, *args, **kvargs)







