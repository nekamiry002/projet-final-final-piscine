from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.views import View
from django.template import loader
from django.contrib.auth.decorators  import login_required #--> import @login_required
from django.contrib.auth.forms import AuthenticationForm


from .form import PostForm
from .form import RechercheForm


from .models import Jeux
from .models import Post
from .models import Recherche

from django.contrib.auth.models import User

class Liste_jeux(View):
    def get(self, request):
        formulaire_recherche = RechercheForm(request.GET)
        if formulaire_recherche.is_valid():

            recherche = formulaire_recherche.cleaned_data['recherche']

            date = formulaire_recherche.cleaned_data['date']
            if date == None:
                resultats = Jeux.objects.all()
            else:
                resultats = Jeux.objects.filter(date__gt=date).filter(name__icontains=recherche)

            formulaire_recherche = RechercheForm()

            return render(request, 'main_site/liste_jeux.html', {'jeux': resultats, 'terme_recherche': recherche,'formulaire_recherche': formulaire_recherche})
        else:
            resultats = Jeux.objects.all()
            formulaire_recherche = RechercheForm()
            return render(request, 'main_site/liste_jeux.html', {'formulaire_recherche': formulaire_recherche , 'jeux': resultats })
    


class Details_jeu(View):
    def get(self, request, jeu_id):
        jeux = Jeux.objects.all()
        if jeu_id<=jeux.count() :
            jeu= jeux[jeu_id -1]
            print(jeu)
        else:
            jeu= None
            return HttpResponseNotFound
        avis = Post.objects.filter(jeux=jeu)

        form = PostForm()
        context = {
            'jeu': jeu,
            'PostForm': form, 
            'AuthForm': AuthenticationForm,
            'jeu_id': jeu_id,
            'avis':avis,
        }
        return render(request, 'main_site/details_jeu.html', context)

    def post(self, request, jeu_id):
        jeux = Jeux.objects.all()
        if jeu_id<=jeux.count() :
            jeu= jeux[jeu_id -1]
        else:
            jeu= None
            return HttpResponseNotFound
        print('oui')
        form = PostForm(request.POST) #ou PostModelForm() etc...
        if form.is_valid():
            avis = form.cleaned_data['avis']
            note = form.cleaned_data['note']
            Post.objects.create(**form.cleaned_data, author = request.user, jeux = jeu)
            return redirect('details_jeu', jeu_id=jeu_id)
        else:
            print('error')
        context = {
            'jeu': jeu,
            'PostForm': form, 
            'AuthForm': AuthenticationForm,
            'jeu_id': jeu_id
        }
        return render(request, 'main_site/details_jeu.html', context)

 #   def delete (self, request, jeu_id):
 #       jeux = Jeux.objects.all()
 #       if jeu_id<=jeux.count() :
 #           jeu= jeux[jeu_id -1]
 #       else:
 #           jeu= None
 #           return HttpResponseNotFound
 #       form = PostForm()
 #       context = {
 #           'jeu': jeu,
 #           'PostForm': form, 
 #           'AuthForm': AuthenticationForm,
 #           'jeu_id': jeu_id
 #       }
 #       return render(request, 'main_site/details_jeu.html', context)




def supprimer_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    # Vérifier si l'utilisateur actuel est l'auteur du post
    if request.user == post.author:
        jeu_id = post.jeux.id
        post.delete()
        return redirect('details_jeu', jeu_id=jeu_id)
    else:
        return ('Error')




class Home_page(View):
    def get(self, request):
        jeux = Jeux.objects.all()
        print(jeux.count())
        print(jeux.count()>=5)
        if jeux.count()>=5:
            nouveautes = Jeux.objects.all().order_by('-date')[:5]
            nouveautes = list(nouveautes)[::-1]
            print(nouveautes)
        else:
            nouveautes = None
        print(nouveautes)
        context = {
            'jeux': jeux ,
            'nouveautes':nouveautes
        }
        return render(request, 'main_site/Home_page.html', context)