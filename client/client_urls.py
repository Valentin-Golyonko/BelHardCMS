from django.urls import path

from . import views

urlpatterns = [
    path('', views.client_main_page, name='client'),  # main client page
    path('profile', views.client_profile, name='client_profile'),
    path('edit', views.client_edit_main, name='client_edit'),
    path('edit/skills', views.client_edit_skills, name='client_edit_skills'),
    path('edit/experience', views.client_edit_experience, name='client_edit_experience'),
    # request.POST == save data
    # TODO: есть ли лучший метод обработки POST ?
    path('save_edit_main', views.save_client_edit_main, name='client_save_edit_main'),
    path('save_edit_skills', views.save_client_edit_skills, name='client_save_edit_skills'),
    path('save_edit_experience', views.save_client_edit_experience, name='client_save_edit_experience'),
]
