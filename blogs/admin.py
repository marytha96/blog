from django.contrib import admin
from .models import   BlogBackgroundImage,Instagram, BlogDetail, About, IndexBackgroundImage, Slider




class BlogBackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'bg_image_blog',

                    ]
class SliderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'slide_image',
                      'slide_title',
                        'slide_sub_title',
                          'slide_text',
                            'slide_facebook',
                              'slide_twitter',
       'slide_instagram',

                              'slide_linkedIn',


                    ]
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'bg_image_about',
                      'bg_image_1',
                        'personal_image_about',
                          'desc1',
                            'desc2',
                              'text_quotations',

                    ]

                    
class IndexBackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'bg_image_index',

                    ]

class InstagramAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'insta_facebook1',
                    'insta_facebook2',
                    'insta_facebook3',
                    'insta_facebook4',
                    'insta_facebook5',
                    'insta_facebook6',
                    'insta_desc',
                    'insta_hash',
                   
                    ]

admin.site.register(BlogDetail)
admin.site.register(Instagram, InstagramAdmin)

admin.site.register(About, AboutAdmin)
admin.site.register(Slider, SliderAdmin)


admin.site.register(IndexBackgroundImage, IndexBackgroundImageAdmin)

admin.site.register(BlogBackgroundImage, BlogBackgroundImageAdmin)