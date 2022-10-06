from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

#custom check
@user_passes_test(lambda user: user.username == 'reinaldo')
def reinaldoview(request):
    return render(request, 'article/article_reinaldo.html')


#simple decorator check
@user_passes_test(lambda user: Group.objects.get(name='writer') in user.groups.all())
def artikelAddView2(request):

    context = {
        'page_title' : 'Tambah Artikel View 2',

    }

    return render(request, 'article/article_add.html', context)


#decorator check
def checkwriter(user):
    test_group = Group.objects.get(name='writer')
    user_group = user.groups.all()

    status = test_group in user_group
    return status


@user_passes_test(checkwriter)
def artikelAddView(request):

    context = {
        'page_title' : 'Tambah Artikel View',

    }

    return render(request, 'article/article_add.html', context)



#internal check
def artikelIndexView(request):
    context = {
        'page_title' : 'Article'
    }

    test_group = Group.objects.get(name='writer')
    user_group = request.user.groups.all()

    template_name = None

    if test_group in user_group:
        #logic for user inside group
        template_name = 'article/index_writer.html'
    else:
        #logic for user outside group
        template_name = 'article/index_reader.html'

    return render(request, template_name, context)