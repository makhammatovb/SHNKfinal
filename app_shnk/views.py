from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .filters import SHNKGroupsFilter, SHNKDocumentsFilter, SHNKPartsFilter
from .models import SHNKSystemsModel, SHNKGroupsModel, SHNKTypesModel, SHNKDocumentsModel, SHNKPartsModel
from .serializers import (SHNKSystemsSerializer, SHNKSystemsGETSerializer,
                          SHNKGroupsSerializer, SHNKGroupsGETSerializer,
                          SHNKTypesSerializer,
                          SHNKDocumentsSerializer, SHNKDocumentsGETSerializer,
                          SHNKPartsSerializer, SHNKPartsGETSerializer)
from .permissions import IsSuperUserOrReadOnly

# Create your views here.
class SHNKSystemsViewSet(ModelViewSet):
    queryset = SHNKSystemsModel.objects.all()
    permission_classes = [IsSuperUserOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SHNKSystemsGETSerializer
        return SHNKSystemsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


class SHNKGroupsViewSet(ModelViewSet):
    queryset = SHNKGroupsModel.objects.all()
    permission_classes = [IsSuperUserOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SHNKGroupsFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SHNKGroupsGETSerializer
        return SHNKGroupsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return serializer.save


class SHNKTypesViewSet(ModelViewSet):
    queryset = SHNKTypesModel.objects.all()
    permission_classes = [IsSuperUserOrReadOnly]
    serializer_class = SHNKTypesSerializer


class SHNKDocumentsViewSet(ModelViewSet):
    queryset = SHNKDocumentsModel.objects.all()
    permission_classes = [IsSuperUserOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SHNKDocumentsFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SHNKDocumentsGETSerializer
        return SHNKDocumentsSerializer

class SHNKPartsViewSet(ModelViewSet):
    queryset = SHNKPartsModel.objects.all()
    permission_classes = [IsSuperUserOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SHNKPartsFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SHNKPartsGETSerializer
        return SHNKPartsSerializer
