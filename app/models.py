from django.db import models

# Create your models here.


class Imagepost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head1 = models.CharField(max_length=500, default="")
    chead1 = models.CharField(max_length=5000, default="")
    tags = models.CharField(max_length=50, default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to='app/images/', default="")

    def __str__(self):
        return self.title
