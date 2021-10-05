from django.db import models
from .validators import validate_image_extension
from django.utils.translation import gettext_lazy as _

from datetime import date


class BlogBackgroundImage(models.Model):
    id = models.BigAutoField(primary_key=True)

    bg_image_blog = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/',default='', blank=True)


class Slider(models.Model):
    id = models.BigAutoField(primary_key=True)

    slide_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', blank=True, )
    slide_title = models.CharField(
        max_length=300, default='', blank=True, )
    slide_sub_title = models.CharField(
        max_length=300, default='', blank=True, )
    slide_text = models.CharField(
        max_length=300, default='', blank=True, )
    slide_facebook = models.CharField(
        max_length=300, default='', blank=True, )
    slide_twitter = models.CharField(
        max_length=300, default='', blank=True, )
    slide_instagram = models.CharField(
        max_length=300, default='', blank=True, )
    slide_linkedIn = models.CharField(
        max_length=300, default='', blank=True, )

class Instagram(models.Model):
    id = models.BigAutoField(primary_key=True)

    insta_facebook1 = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', blank=True, )
    insta_facebook2 = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', blank=True, )
    insta_facebook3 = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', blank=True, )
    insta_facebook4 = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', blank=True, )
    insta_facebook5 = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', blank=True, )
    insta_facebook6 = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', blank=True, )
    insta_desc = models.CharField(
        max_length=300, default='', blank=True, )
    insta_hash = models.CharField(
        max_length=300, default='', blank=True, )
class About(models.Model):
    id = models.BigAutoField(primary_key=True)

    bg_image_about = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/',default='', blank=True)
    bg_image_1 = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/',default='', blank=True)

    personal_image_about = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/',default='', blank=True)

    desc1 = models.TextField(
        max_length=1000, default='', blank=True)
    desc2 = models.TextField(
        max_length=1000, default='', blank=True)
    text_quotations = models.TextField(
        max_length=1000, default='', blank=True)
       


class IndexBackgroundImage(models.Model):

    id = models.BigAutoField(primary_key=True)

    bg_image_index = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/',default='', blank=True)
  



class BlogDetail(models.Model):
    id = models.BigAutoField(primary_key=True)


    blog_image_one = models.FileField(
        validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)
    blog_image_two = models.FileField(
        validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)
    blog_image_three = models.FileField(
        validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)

    blog_date = models.DateField(default=date.today, blank=True)
   
    blog_name = models.CharField(
        max_length=300, default='', blank=True)
    blog_desc1 = models.CharField(
        max_length=120, default='', blank=True)
    blog_desc2 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_desc3 = models.TextField(
        max_length=1000, default='', blank=True)
   
    blog_desc5 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_desc6 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_desc7 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_desc_insatll_1 = models.CharField(
        max_length=300, default='', blank=True)
    blog_title_1 = models.CharField(
        max_length=300, default='', blank=True)
    blog_title_1_desc1 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_title_1_desc2 = models.TextField(
        max_length=300, default='', blank=True)
    blog_desc_insatll_package_3 = models.CharField(
        max_length=300, default='', blank=True)
    blog_desc_insatll_package_4 = models.CharField(
        max_length=300, default='', blank=True)
    blog_desc_insatll_package_5 = models.CharField(
        max_length=300, default='', blank=True)
    blog_image_blog_title_1desc_1 = models.FileField(validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)

    blog_title_2 = models.CharField(
        max_length=300, default='', blank=True)

    blog_title_2_desc1 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_image_blog_title_2_desc1 = models.FileField(validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)
    blog_title_2_desc2 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_image2_blog_title_2_desc1 = models.FileField(validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)

    blog_title_3 = models.CharField(
        max_length=300, default='', blank=True)
    blog_title_3_desc1 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_image_blog_title_3_desc1 = models.FileField(validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)

    blog_title_4 = models.CharField(
        max_length=300, default='', blank=True)
    blog_title_4_desc1 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_title_4_desc2 = models.TextField(
        max_length=1000, default='', blank=True)

    blog_image_blog_title_4_desc1 = models.FileField(validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)
    blog_image2_blog_title_4_desc1 = models.FileField(validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)

    blog_title_5 = models.CharField(
        max_length=300, default='', blank=True)
    blog_title_5_desc1 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_image_blog_title_5_desc1 = models.FileField(validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)
    note = models.TextField(
        max_length=1000, default='', blank=True)
    note_image = models.FileField(validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)

    note1 = models.TextField(
        max_length=1000, default='', blank=True)
    note_image_1 = models.FileField(validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)

    blog_desc4 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_desc4_image_1 = models.FileField(validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)
    blog_resourse1 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_resourse2 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_resourse3 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_resourse4 = models.TextField(
        max_length=1000, default='', blank=True)
    blog_resourse5 = models.TextField(
        max_length=1000, default='', blank=True)
  
    class Meta:
        ordering = ['-blog_date']

