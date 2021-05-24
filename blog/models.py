from django.db import models
from django.db.models.fields import TextField


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = TextField()
    image = models.ImageField(upload_to ='images/')

    #This returns the title of the blog page in admin/blog/blog
    def __str__(self):
        return self.title

    #This limit the the number of the next in the body
    def summary(self):
        return self.body[:100]

    #This will only return the date in the blog page
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
