from rest_framework.serializers import ModelSerializer, SerializerMethodField

from app_shnk.models import (SHNKSystemsModel,
                             SHNKGroupsModel,
                             SHNKTypesModel,
                             SHNKDocumentsModel, SHNKPartsModel,
                             )



class SHNKSystemsSerializer(ModelSerializer):

    class Meta:
        model = SHNKSystemsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True}
        }


class SHNKSystemsGETSerializer(ModelSerializer):
    system_name = SerializerMethodField(method_name='get_system_name', read_only=True)

    class Meta:
        model = SHNKSystemsModel
        fields = ('id', 'code', 'system_name')

    def get_system_name(self, obj):
        try:
            if self.context['request']['lang'] == 'ru':
                return obj.system_name_ru
            return obj.system_name_uz
        except:
            return obj.system_name_uz


class SHNKGroupsSerializer(ModelSerializer):

    class Meta:
        model = SHNKGroupsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }


class SHNKGroupsGETSerializer(ModelSerializer):
    group_name = SerializerMethodField(method_name='get_group_name', read_only=True)

    class Meta:
        model = SHNKGroupsModel
        fields = ('id', 'group_code', 'group_name')

    def get_group_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.system_name_ru
            return obj.system_name_uz
        except:
            return obj.system_name_uz


class SHNKTypesSerializer(ModelSerializer):

    class Meta:
        model = SHNKTypesModel
        fields = '__all__'


class SHNKDocumentsSerializer(ModelSerializer):

    class Meta:
        model = SHNKDocumentsModel
        fields = '__all__'


class SHNKDocumentsGETSerializer(ModelSerializer):
    shnk_name = SerializerMethodField(method_name='get_documents', read_only=True)

    class Meta:
        model = SHNKDocumentsModel
        fields = ('id', 'shnk_code', 'shnk_name')


    def get_documents(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.shnk_name_ru
            return obj.shnk_name_uz
        except:
            return obj.shnk_name_uz


class SHNKPartsSerializer(ModelSerializer):

    class Meta:
        model = SHNKPartsModel
        fields = '__all__'


class SHNKPartsGETSerializer(ModelSerializer):
    shnk_part = SerializerMethodField(method_name='get_part', read_only=True)

    class Meta:
        model = SHNKPartsModel
        fields = ('id', 'shnk_part')

    def get_part(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.part_title_ru
            return obj.part_title_uz
        except:
            return obj.part_title_uz