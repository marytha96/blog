from django.shortcuts import render
from .models import  BlogBackgroundImage, BlogDetail,Instagram, About, IndexBackgroundImage, Slider
from .serializers import  BlogDetailSerializer, AboutSerializer, IndexBackgroundImageSerializer
from django.http import HttpRequest
from django.http import HttpResponse

# from .filters import BlogDetailFilter
from .form import BlogDetailForm
from django.core.mail import send_mail,  EmailMessage
from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.core.paginator import Paginator

def blog_list(request):

    blog = BlogDetail.objects.all().order_by('-blog_date')
    blogBackgroundImage = BlogBackgroundImage.objects.all()
    # filters
    # myfilter = BlogDetailFilter(request.GET, queryset=blog)
    # blog = myfilter.qs
    # Show many contacts per page.
    paginator = Paginator(blog, 10000000000000000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if blog:
        context = {'blog': page_obj, 'myfilter': blog,
        'blogBackgroundImage':blogBackgroundImage}  # template name

    else:
        context = {'message': "There are no stories available at the moment."}
    return render(request, 'stories.html', context)


def blog_detail(request, id):
    """Renders the create volunteer page."""
    blog = BlogDetail.objects.get(id=id)

    context = {'blog': blog}
    return render(request, 'stories_detail.html', context)
def about(request):
    """Renders the create about page."""
    assert isinstance(request, HttpRequest)
    queryset = About.objects.all()
    serializer_class = AboutSerializer(queryset, many=True)

    return render(request, 'about.html',
                  {
                      'data': serializer_class.data,
                  }
                  )



def contact(request):
    if request.method == 'POST':
        print("hello")
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = {
            'name': name,
            'email' : email,
            'message' : message,
        }
        print(data)
      
        message = ''' 
        New message :{}
        From: {}
        '''.format(data['message'], data['email'])

        if name and message and email:
            try:
                send_mail(data['name'], message, from_email= 'techs.maryam@gmail.com',recipient_list= ['tecdhs.maryam@gmail.com'],  fail_silently=False)

            except  Exception as error:
                return HttpResponse('Invalid header found.')
    return render(request, 'contact.html')


def index(request):
    """Renders the create index page."""
    assert isinstance(request, HttpRequest)
    queryset = IndexBackgroundImage.objects.all()
    serializer_class = IndexBackgroundImageSerializer(queryset, many=True)
    slider_show = Slider.objects.all()[:4]
    instagram = Instagram.objects.all()
    blog = BlogDetail.objects.all()

    # Show many contacts per page for stories
    paginator_blog = Paginator(blog, 10000000000000000)
    page_number_blog = request.GET.get('page')
    page_obj_blog = paginator_blog.get_page(page_number_blog)
    context = {
        'data': serializer_class.data,
        'slider_show': slider_show,
       'instagram':instagram,
               'blog': page_obj_blog,

    }
    return render(request, 'index.html',context
                 
                  )
