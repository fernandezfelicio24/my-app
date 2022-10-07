from django.db import models
from django.utils.text import slugify
from django.utils import timezone


# Create your models here.
class SportArticle(models.Model):
    title     = models.CharField(max_length=255)
    paragraph = models.TextField()
    created   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(null=True)
    published = models.DateTimeField(null=True)
    slug      = models.SlugField(blank=True, editable=False)

    #add manual permission
    class Meta :
        #default_permission = ('add', 'change', 'delete')
        permissions = (
            ('publish_article', 'Can publish article'),
        )

    def save(self):
        self.slug = slugify(self.title)

        if self.is_published == True:
            self.published = timezone.now()
        else:
            self.published = None

        super().save()

    def __str__(self):
        return "{}. {}".format(self.id, self.title)