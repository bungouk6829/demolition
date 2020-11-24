from django.db import models

class Result_post(models.Model):

    text = models.TextField(max_length=5000, blank=True, null=True)
    address = models.CharField(max_length=200)
    business_name = models.CharField(max_length=200)
    business_start_at = models.DateField(null=True, blank=True)
    business_finish_at = models.DateField(null=True, blank=True)
    file_1 = models.FileField(upload_to='files/', null=True, blank=True)
    file_2 = models.FileField(upload_to='files/', null=True, blank=True)
    file_3 = models.FileField(upload_to='files/', null=True, blank=True)
    file_4 = models.FileField(upload_to='files/', null=True, blank=True)
    file_5 = models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return self.address

    class Meta:
        db_table = 'result_posts'

class Notice_post(models.Model):

    title = models.CharField(max_length=50)
    text = models.TextField(max_length=5000, blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    clicks = models.IntegerField(default=1)
    file_1 = models.FileField(upload_to='files/', null=True, blank=True)
    file_2 = models.FileField(upload_to='files/', null=True, blank=True)
    file_3 = models.FileField(upload_to='files/', null=True, blank=True)
    file_4 = models.FileField(upload_to='files/', null=True, blank=True)
    file_5 = models.FileField(upload_to='files/', null=True, blank=True)


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

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'information_posts'
