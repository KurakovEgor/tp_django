from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView

from questions.models import Article, Comment, UserProfile

class UserForm(forms.Form):

    def clear(self):
        pass #TODO
#        if password1 == password2:
#            self.cleaned_data['password1'] = password1
#            self.cleaned_data['password2'] = password2
#        else:
#            raise
    login = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'ivanov1949', "maxlength" : "32"}))

    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'ivanov1949@example.com'}))

    username = forms.CharField(widget = forms.TextInput(attrs={"class " : "form-control", 'placeholder' : 'Alex Ivanov' }))#max_length = 255)

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : '******'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : '******'}))

    avatar = forms.ImageField(widget=forms.FileInput(attrs={"accept" : "image/gif, image/png, image/jpg"}))

#    birthday = forms.DateField(
#                               initial="2015-01-01",
#                               widget=forms.TextInput(attrs={"class":"form-control", "placeholder" : "2015-01-01"}),
#                              )

class LoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'ivanov1949'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'class' : 'form-control'}))
       
    class Meta:
        fields = ('login', 'password')


class ArticleForm(forms.Form): #(forms.ModelForm): 
    class Meta:
#        model = Article
#        exclude = []
        field = ('title', 'text', 'tags')
      

    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'maxlength' : '255'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
#    author = forms.ForeignKey(UserProfile)
#    rating = forms.IntegerField(default=0, verbose_name="Рейтинг")
    tags = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
#    picture = models.ImageField(
#                                upload_to="article_picture/%Y/%m/%d",
#                                null=True, blank=True,
#                                verbose_name="Картинка",
#                               )

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))
