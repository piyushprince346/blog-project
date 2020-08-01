from django.db import models

from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

TOPIC_CHOICES = (
    ('Web Development','Web Development'),
    ('App Development','App Development'),
    ('Politics','Politics'),
    ('Mental Health','Mental Health'),
    ('Travel','Travel'),
    ('Social Issues','Social Issues'),
    ('College Experience','College Experience'),
    ('Photography','Photography'),
    ('Wildlife','Wildlife'),
    ('Natural Disaster Management','Natural Disaster Management'),
    ('Lifestyle','Lifestyle'),
    ('Fitness And Workout','Fitness And Workout'),
    ('Competitive Programming','Competitive Programming'),
    ('Astrology','Astrology'),
    ('Science And Research','Science And Research'),
    ('Others','Others')
)

class Blogpost(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    topic = models.CharField(max_length=50,choices=TOPIC_CHOICES,default='Others')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment = True)

    def get_absolute_url(self):
        return reverse("blog:blog_details", kwargs={"pk": self.pk})

    def datepublished(self):
        return self.published_date.strftime('%B %d %Y')
    
    def datecreated(self):
        return self.create_date.strftime('%B %d %Y')
    
    def __str__(self):
        return self.topic + ': ' +  self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Blogpost,on_delete=models.CASCADE,related_name='comments')
    author = models.CharField( max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def datepublished(self):
        return self.create_date.strftime('%B %d %Y')

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.post.pk})
    

    def __str__(self):
        return self.text
    



