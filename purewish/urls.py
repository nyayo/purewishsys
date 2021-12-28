from django.urls import path
from .views import UserPostListView
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('search', views.view_donor, name='search-home'),
    path('all_post/', views.all_post, name='all-post'),
    path('add_post/', views.add_post, name='add-post'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('update_post/<str:id>/', views.update_post, name='update-post'),
    path('delete_post/<str:id>/', views.delete_post, name='delete-post'),

    path('view_donor/', views.view_donor, name='view-donor'),
    path('add_donor/', views.add_donor, name='add-donor'),
    path('update_donor/<str:id>/', views.update_donor, name='update-donor'),
    path('delete_donor/<str:id>/', views.delete_donor, name='delete-donor'),
    path('donor_contact/', views.donor_contact, name='donor-contact'),

    path('all_messages/', views.all_messages, name='all-msg'),
    path('user_messages/<str:id>/', views.user_messages, name='user-msg'),
    path('message_staff/', views.message_staff, name='msg-staff'),
    path('message_donor/', views.message_donor, name='msg-donor'),
    path('direct_chat/', views.direct_chat, name='direct-chat'),

    path('available_staff/', views.available_staff, name='all-staffs'),
    path('add_staff/', views.add_staff, name='add-staff'),
    path('update_stuff/<str:id>/', views.update_stuff, name='update-stuff'),
    path('delete_stuff/<str:id>/', views.delete_stuff, name='delete-stuff'),
    path('staffs_contact/', views.staffs_contact, name='staffs-contact'),

    path('all_volunteers/', views.all_volunteers, name='all-volunteers'),
    path('update_volunteer/<str:id>/',
         views.update_volunteer, name='update-volunteer'),
    path('delete_volunteer/<str:id>/',
         views.delete_volunteer, name='delete-volunteer'),
    path('add_volunteers/', views.add_volunteers, name='add-volunteers'),
    path('volunteers_contact/', views.volunteers_contact,
         name='volunteers-contact'),

    path('calender/', views.calender, name='calendar'),
    path('gallery/', views.gallery, name='gallery'),

    path('view_projects/', views.view_projects, name='view-project'),
    path('project_detail/<str:id>/', views.project_detail, name='project-detail'),
    path('delete_project/<str:id>/', views.delete_project, name='delete-project'),
    path('update_project/<str:id>/', views.update_project, name='update-project'),
    path('add_project/', views.add_project, name='add-project'),

    path('mail_inbox/', views.mail_inbox, name='mail-inbox'),
    path('compose_mail/', views.compose_mail, name='compose-mail'),
    path('read_mail/', views.read_mail, name='read-mail'),

    path('login/', views.userLogin, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register')
]
