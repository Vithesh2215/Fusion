from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import include
from django.contrib import admin
from django.conf.urls import url, include

app_name = 'hostelmanagement'

urlpatterns = [

    path('admin/', admin.site.urls),
    #Home 
    path('', views.hostel_view, name="hostel_view"),
    path('/hello', views.hostel_view, name="hello"),

    #Notice Board
    path('notice_form/', views.notice_board, name="notice_board"),
    path('delete_notice/', views.delete_notice, name="delete_notice"),

    #Worker Schedule
    path('edit_schedule/', views.staff_edit_schedule, name='staff_edit_schedule'),
    path('delete_schedule/', views.staff_delete_schedule, name='staff_delete_schedule'),
    
    #Student Room
    path('edit_student/',views.edit_student_room,name="edit_student_room"),
    path('edit_student_rooms_sheet/', views.edit_student_rooms_sheet, name="edit_student_rooms_sheet"),

    #Attendance
    path('edit_attendance/', views.edit_attendance, name='edit_attendance'),

    #Attendance
    path('edit_attendance/', views.edit_attendance, name='edit_attendance'),

    #Worker Report
    path('worker_report/', views.generate_worker_report, name='workerreport'),
    path('pdf/', views.GeneratePDF.as_view(), name="pdf"),



    #for superUser

    path('hostel-notices/', views.hostel_notice_board, name='hostel_notices_board'),
    # //caretaker and warden can see all leaves
    path('all_leave_data/', views.all_leave_data, name='all_leave_data'),
    # //apply for leave
    path('create_hostel_leave/', views.create_hostel_leave.as_view(), name='create_hostel_leave'),
    # caretaker and warden can get all complaints
    path('hostel_complaints/', views.hostel_complaint_list, name='hostel_complaint_list'),
    # only user can see its complaints
    path('user_complaints/<str:roll_number>/', views.UserComplaints.as_view(), name='user_complaints'),
    # //register complaint
    path('register_complaint/', views.PostComplaint.as_view(), name='PostComplaint'),

    # //////////////////////

    path('hostel_complaint_list/', views.hostel_complaint_list, name='hostel_complaint_list'),



    path('assign-batch/', views.AssignBatchView.as_view(),name='AssignBatchView'),
    path('hall-ids/', views.HallIdView.as_view(), name='hall'),
    path('assign-caretaker', views.AssignCaretakerView.as_view(), name='AssignCaretakerView'),
    path('assign-warden',views.AssignWardenView.as_view(), name='AssignWardenView'),
    path('add-hostel', views.AddHostelView.as_view(), name='add_hostel'),
    path('admin-hostel-list', views.AdminHostelListView.as_view(), name='admin_hostel_list'),  # URL for displaying the list of hostels
    path('delete-hostel/<str:hall_id>/', views.DeleteHostelView.as_view(), name='delete_hostel'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='logout_view'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  
    # !! My Change
    path('allotted_rooms/<str:hall_id>/', views.alloted_rooms, name="alloted_rooms"),

    path('all_staff/<int:hall_id>/', views.all_staff, name='all_staff'),
    path('staff/<str:staff_id>/', views.StaffScheduleView.as_view(), name='staff_schedule'),
    
    # path('inventory/hallList/', views.inventory_handle_table, name='hall_list'),
    path('inventory/', views.HostelInventoryView.as_view(), name='hostel_inventory_list'),
    path('inventory/<int:inventory_id>/modify/', views.HostelInventoryUpdateView.as_view(), name='hostel_inventory_update'),
    path('inventory/<int:inventory_id>/delete/', views.HostelInventoryView.as_view(), name='hostel_inventory_detail'),
    path('inventory/<int:hall_id>/', views.HostelInventoryView.as_view(), name='hostel_inventory_by_hall'),
    path('inventory/form/', views.get_inventory_form, name='get_inventory_form'),
    path('inventory/edit_inventory/<int:inventory_id>/', views.edit_inventory, name='edit_inventory'),
    path('allotted_rooms/', views.alloted_rooms_main, name="alloted_rooms"),
    path('all_staff/', views.all_staff, name='all_staff')


]