from django.db import models

class Result_post(models.Model):

    title = models.CharField(max_length=50)
    text = models.TextField(max_length=5000, blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    edit_at =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'result_posts'

class Notice_post(models.Model):

    title = models.CharField(max_length=50)
    text = models.TextField(max_length=5000, blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    edit_at = models.DateTimeField(auto_now=True)
    clicks = models.IntegerField(default=1)

    @property
    def update_clicks(self):
        self.clicks += 1
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'notice_posts'

class Information_post(models.Model):

    password = models.CharField(max_length=20)
    author = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=5000)
    phone_number = models.CharField(max_length=20)
    create_at = models.DateField(auto_now_add=True)
    edit_at =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'information_posts'
