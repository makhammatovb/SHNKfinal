import django_filters

from .models import SHNKGroupsModel, SHNKDocumentsModel, SHNKPartsModel

class SHNKGroupsFilter(django_filters.FilterSet):
    group_system = django_filters.CharFilter(lookup_expr='exact', required=True)

    class Meta:
        model = SHNKGroupsModel
        fields = ['group_system']


class SHNKDocumentsFilter(django_filters.FilterSet):
    shnk_documents = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = SHNKDocumentsModel
        fields = ['shnk_documents']


class SHNKPartsFilter(django_filters.FilterSet):
    shnk_parts = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = SHNKPartsModel
        fields = ['shnk_parts']