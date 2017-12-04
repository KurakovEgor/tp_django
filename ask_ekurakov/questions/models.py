# -*-coding : utf-8-*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

class UserProfileManager(models.Manager):
    def with_login(self, login):
        return UserProfile.objects.get(user_username=login)

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=False, primary_key=True, verbose_name = 'Аккаунт')
    username = models.CharField(null = True, max_length=32, verbose_name="Username")
    avatar = models.ImageField(null = True, blank = True, verbose_name='Аватар')
    register_date = models.DateField(default = timezone.now(), null = False, blank = True, verbose_name = "Дата регистрации")
    objects = UserProfileManager()

    def __str__(self):
        return self.username
  
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

class ArticleManager(models.Manager):
    def published(self):
        return Article.objects.filter(is_published=True).order_by("-id")
    
    def best_published(self):
        return Article.objects.filter(is_published=True).order_by("-rating")       
    
    def number_of_comments(self):
        return Comment.numOfCommentsFromArticle(id)

    def with_tag(self, nameOfTag):
        return Tag.objects.get(name=nameOfTag).article_set.all()[:]
            

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name=u"Заголовок")
    text = models.TextField(verbose_name=u"Текст")
    author = models.ForeignKey(UserProfile)
    rating = models.IntegerField(default=0, verbose_name="Рейтинг")
    tags = models.ManyToManyField('Tag')
    picture = models.ImageField(
                                upload_to="article_picture/%Y/%m/%d",
                                null=True, blank=True,
                                verbose_name="Картинка",
                               )
    date = models.DateField(default = timezone.now(), verbose_name = "Дата Добавления")

    is_published = models.BooleanField(
        default=True, verbose_name=u"Опубликована"
    )

    objects = ArticleManager()  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"Статья"
        verbose_name_plural = u"Статьи"

#class Author(models.Model):
#    name = models.CharField(max_length=255,verbose_name=u"Имя")
#    birthday = models.DateField(default = timezone.now())
#
#    def __str__(self):
#        return self.name
#
#    class Meta:
#        verbose_name = u"Автор"
#        verbose_name_plural = u"Авторы"

class CommentManager(models.Manager):
    def numOfCommentsFromArticle(self, idOfArticle):
        return len(Comment.objects.filter(article=idOfArticle))

    def fromArticle(self, idOfArticle):
        return Comment.objects.filter(article=idOfArticle).order_by("-is_correct", "-rating", "id")

class Comment(models.Model):
    text = models.TextField(verbose_name=u"Текст")
    article = models.ForeignKey(Article)
    rating = models.IntegerField(default = 0, verbose_name="Рейтинг")
    published_by = models.ForeignKey(UserProfile, null = True)

    objects = CommentManager()

    is_correct = models.BooleanField(default=False, blank=True, verbose_name=u"Решение")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

#class TagManager(models.Manager):
#    def ArticlesWithTag(self, nameOfTag):
#        a = []
#        for i in Article.objects.all():
#            if (nameOfTag in i.tags):
#                a.append(i)
#            for j in i.tags:
#	    if j.name==nameOfTag:
#                    a.append[i]
#        return
        

class Tag(models.Model):
    name = models.CharField(verbose_name="Тег", max_length=255)
    
#    objects = TagManager()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Like(models.Model):
    like_creator = models.ForeignKey("UserProfile", verbose_name = "Профиль поставившего лайк")
    is_like = models.BooleanField(verbose_name = "Лайк")

    def __str__(self):
        return "Оценка пользователя" + like_creator.username

    class Meta:
        verbose_name = "Оценка пользователя"
        verbose_name_plural = "Оценки пользователей" 


class ArticleLike(Like):
    like_to_article = models.ForeignKey("Article",verbose_name = "Оцениваемая статья")
       
    def __str__(self):
        if (is_like):
            return "Лайк пользователя " + like_creator.username + " к статье " + like_to_article
        else:
            return "Дислайк пользователя " + like_creator.username + " к статье " + like_to_article

    class Meta:
        verbose_name = "Оценка пользователем статьи"

class CommentLike(Like):
    like_to_comment = models.ForeignKey("Comment", verbose_name = "Оцениваемый ответ")
       
    def __str__(self):
        if (is_like):
            return "Лайк пользователя " + like_creator.username + " к ответу " + like_to_comment
        else:
            return "Дислайк пользователя " + like_creator.username + " к ответу " + like_to_comment

    class Meta:
        verbose_name = "Оценка пользователем комментария"
