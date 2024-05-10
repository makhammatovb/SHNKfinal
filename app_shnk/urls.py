from django.urls import path
from rest_framework import routers

from app_shnk.views import (SHNKSystemsViewSet,
                            SHNKGroupsViewSet,
                            SHNKTypesViewSet,
                            SHNKDocumentsViewSet,
                            SHNKPartsViewSet)

router = routers.DefaultRouter()
router.register(r'systems', SHNKSystemsViewSet)
router.register(r'groups', SHNKGroupsViewSet)
router.register(r'types', SHNKTypesViewSet)
router.register(r'documents', SHNKDocumentsViewSet)
router.register(r'parts', SHNKPartsViewSet)

urlpatterns = router.urls
