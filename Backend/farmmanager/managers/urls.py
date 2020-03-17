from rest_framework import routers
from .api import IncomeViewset

router = routers.DefaultRouter()
router.register('api/managers', IncomeViewset, 'managers')

urlpatterns = router.urls
