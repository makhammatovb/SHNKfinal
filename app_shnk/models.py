from django.db import models
from django.contrib.auth import get_user_model

from config import settings


# Create your models here.
class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class SHNKSystemsModel(AbstractBaseModel):
    code = models.CharField(max_length=2, unique=True)
    systems_name_uz = models.CharField(max_length=255, unique=True)
    systems_name_ru = models.CharField(max_length=255, unique=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.systems_name_uz}"

    class Meta:
        db_table = 'shnk_systems'
        verbose_name_plural = 'SHNK Systems'


class SHNKGroupsModel(AbstractBaseModel):
    group_code = models.CharField(max_length=15, unique=True)
    group_name_uz = models.CharField(max_length=255)
    group_name_ru = models.CharField(max_length=255)
    group_system = models.ForeignKey(SHNKSystemsModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group_code} - {self.group_name_uz}"

    class Meta:
        db_table = 'shnk_groups'
        verbose_name_plural = 'SHNK Groups'


class SHNKTypesModel(AbstractBaseModel):
    type_name_uz = models.CharField(max_length=255, unique=True)
    type_name_ru = models.CharField(max_length=255, unique=True, null=True)
    type_description_uz = models.CharField(max_length=255, null=True, blank=True)
    type_description_ru = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.type_name_uz} - {self.type_name_ru}"

    class Meta:
        db_table = 'shnk_types'
        verbose_name_plural = 'SHNK Types'


class SHNKDocumentsModel(AbstractBaseModel):
    shnk_name_uz = models.CharField(max_length=255, unique=True)
    shnk_name_ru = models.CharField(max_length=255, unique=True, null=True)
    shnk_code = models.CharField(max_length=10, unique=True)
    shnk_type = models.ForeignKey(SHNKTypesModel, on_delete=models.CASCADE)
    shnk_file_uz = models.FileField(upload_to='shnk', null=True, blank=True)
    shnk_file_ru = models.FileField(upload_to='shnk', null=True, blank=True)
    shnk_group = models.ForeignKey(SHNKGroupsModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.shnk_name_uz} - {self.shnk_name_ru}"

    class Meta:
        db_table = 'shnk_documents'
        verbose_name_plural = 'SHNK Documents'


class SHNKPartsModel(AbstractBaseModel):
    part_title_uz = models.CharField(max_length=255)
    part_title_ru = models.CharField(max_length=255)
    part_number = models.CharField(max_length=10)
    part_text_uz = models.CharField(max_length=255, null=True, blank=True)
    part_text_ru = models.CharField(max_length=255, null=True, blank=True)
    part_documents = models.ForeignKey(SHNKDocumentsModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.part_title_uz} - {self.part_title_ru}"

    class Meta:
        db_table = 'shnk_parts'
        verbose_name_plural = 'SHNK Parts'