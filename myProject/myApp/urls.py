from django.urls import path, include
from . import views
from .views import admin_view, teacher_qualification, teacher_requests_view, admin_index, approval_pending, create_subcategory,view_subcategories, delete_subcategory
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('courses/', views.courses, name='courses'),
    path('category/', views.category, name='category'),
    path('events/', views.events, name='events'),
    # path('contact/', views.contact, name='contact'),
    path('contact-us/', views.contact_us, name='contact'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('reset/<token>/', views.reset, name='reset'),
    path('teacher/qualification/', views.teacher_qualification, name='teacher_qualification'),
    path('categories/', views.view_categories, name='view_categories'),
    path('add_product_rent/', views.add_product_rent, name='add_product_rent'),
    path('add_product_buy/', views.add_product_buy, name='add_product_buy'),
    path('teacher_requests/', views.teacher_requests_view, name='teacher_requests'),
    path('approve_request/<int:request_id>/', views.approve_request, name='approve_request'),
    path('reject_request/<int:request_id>/', views.reject_request, name='reject_request'),
    path('accept_teacher/', views.accept_teacher, name='accept_teacher'),
    path('reject_teacher/', views.reject_teacher, name='reject_teacher'),
    path('accounts/', include('allauth.urls')),
    path('approval_pending/', views.approval_pending, name='approval_pending'),
    path('approve_request/<int:request_id>/', views.approve_request, name='approve_request'),
    path('reject_request/<int:request_id>/', views.reject_request, name='reject_request'),
    path('teacher-requests/', views.teacher_requests_view, name='teacher_requests'),
    path('add-category/', views.add_category, name='add_category'),
    path('view-categories/', views.view_categories, name='view_categories'),  # Assuming you have a view_categories view
    path('edit_category/<int:id>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:id>/', views.delete_category, name='delete_category'),
    path('add_subcategory/', views.add_subcategory, name='add_subcategory'),
    path('create_subcategory/', create_subcategory, name='create_subcategory'),
    path('profile/', views.profile, name='profile'),
    path('view-subcategories/', view_subcategories, name='view_subcategories'),
    path('delete-subcategory/<int:subcategory_id>/', delete_subcategory, name='delete_subcategory'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('student-details/', views.student_details, name='student_details'),
    

    path('admin-contact/', views.admin_contact_us_view, name='admin_contact'),
    path('admin-contact-delete/<int:id>/', views.admin_delete_contact_us_view, name='admin_contact_delete'),

    path('teacher_home', views.teacher_home, name='teacher_home'),
    path('teacher-course-sub-category/<int:id>/', views.teacher_pick_subcategory, name='teacher_subcategory'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
