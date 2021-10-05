from rest_framework import serializers
from .models import BlogBackgroundImage, BlogDetail, About, IndexBackgroundImage, Slider, Instagram



class BlogBackgroundImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogBackgroundImage
        fields = '__all__'

class InstagramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instagram
        fields = '__all__'



class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = '__all__'

class IndexBackgroundImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndexBackgroundImage
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = '__all__'

class BlogDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogDetail
        fields = '__all__'
        ordering = ['-blog_date']
