from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route = '', view = views.get_dealerships, name = 'index'),

    # path for about view
    path(route = 'about/', view = views.about, name = 'about'),
    # path for contact us view
    path(route = 'contact/', view = views.contact, name = 'contact'),
    # path for registration
    path(route = 'signup/', view = views.signup, name = 'signup'),
    # path for login
    path(route = 'login/', view = views.login, name = 'login'),
    # path for logout
    path(route = 'logout/', view = views.logout, name = 'logout'),
    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view
    path('dealer/<int:dealerId>/', views.get_dealer_details, name='dealer_details'),
    # path for add a review view
    path('post_review/<int:dealerId>', views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)