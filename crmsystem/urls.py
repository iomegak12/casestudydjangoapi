from rest_framework_mongoengine import routers
from crmsystem.views import CustomersView

router = routers.DefaultRouter()
router.register(r'crmsystem', CustomersView)

urlpatterns = []
urlpatterns += router.urls
