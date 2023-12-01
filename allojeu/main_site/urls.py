from django.urls import path, include


from .views import Liste_jeux
from .views import Details_jeu
from .views import Home_page
from .views import supprimer_post

urlpatterns = [
    path('', Home_page.as_view(), name='Home'),
    path('contact/', include('contact.urls')),
    path('details/<int:jeu_id>', Details_jeu.as_view(), name='details_jeu'),
    path('all_game/', Liste_jeux.as_view(), name='liste_jeux'),
    path('supprimer_post/<int:post_id>/', supprimer_post, name='supprimer_post'),
]