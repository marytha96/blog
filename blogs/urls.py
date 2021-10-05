from django.urls import path
from . import views
from . import api

app_name = 'blogs'

urlpatterns = [
    # path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
        path('about/', views.about, name='about'),
        path('', views.blog_list, name='index'),


    path('blog_detail/<int:id>', views.blog_detail, name='blog_detail'),

    # api
    path('api/blogs', api.stories_api, name='stories_api'),
    path('api/blogs/<int:id>', api.story_detail_api, name='blog_detail_api'),


    # class based views
    path('api/v2/blogs', api.StoryDetailListApi.as_view(),
         name='BlogsDetailListApi'),
    path('api/v2/blogs/<int:id>',
         api.StoryDetailDetail.as_view(), name='BlogsDetailDetail'),
]
