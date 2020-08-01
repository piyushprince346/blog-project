from django.urls import path,include

from blog import views

app_name = 'blog'

urlpatterns = [
    path('about/',views.AboutView.as_view(),name = 'about'),
    path('',views.BlogpostListView.as_view(),name = 'blogs_list'),
    path('filter/<str:topic_name>/',views.FilterView.as_view(),name = 'filter'),
    path('post/<int:pk>/',views.BlogpostDetailView.as_view(),name = 'blog_details'),
    path('post/create_post/',views.CreateBlogpostView.as_view(),name = 'new_post'),
    path('post/<int:pk>/edit_post/',views.UpdateBlogpostView.as_view(),name = 'edit_post'),
    path('post/<int:pk>/remove_post',views.DeleteBlogpostView.as_view(),name = 'delete_post'),
    path('drafts/',views.DraftListView.as_view(),name = 'drafts'),
    path('post/<int:pk>/add_comment/',views.adding_comment,name = 'add_comment'),
    path('comment/<int:pk>/approve/',views.approve_comments,name = 'approve_comment'),
    path('comment/<int:pk>/delete/',views.remove_comment,name = 'delete_comment'),
    path('post/<int:pk>/publish/',views.publish_post,name = 'publish_post')
]
