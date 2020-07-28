from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about_us"),
    path('contact',views.contact,name="contact_us"),
    path('view_contact',views.view_contact,name='view_contact'),
    path('delete_query/<int:id>',views.delete_query,name="destroy6"),
    path('login',views.Login,name="login"),
    path('Logout',views.logout_admin,name='logout'),
    path('add_enquiry',views.add_enquiry,name='add_enquiry'),
    path('view_enquiry',views.view_enquiry,name='view_enquiry'),
    path('delete_enq/<int:id>', views.delete_enquiry, name='destroy'),
    path('add_equipment',views.add_equipment,name='add_equipment'),
    path('view_equipment',views.view_equipment,name='view_equipment'),
    path('delete_equip/<int:id>', views.delete_equipment, name='destroy1'),

    path('add_plan',views.add_plan,name='add_plan'),
    path('view_plan',views.view_plan,name='view_plan'),
    path('delete_plan/<int:id>', views.delete_plan, name='destroy2'),

    path('add_member', views.add_member, name='add_member'),
    path('view_member', views.view_member, name='view_member'),
    path('delete_member/<int:id>', views.delete_member, name='destroy3'),
    path('hero_section',views.hero_section,name='landingpage'),

]