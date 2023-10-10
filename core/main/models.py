from django.db import models

class GeneralSlider(models.Model):
    img = models.ImageField('Image',upload_to='media')
    title = models.CharField('Slide Title', max_length=255)
    text = models.TextField('Slide Text')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'General Slider'
        verbose_name_plural = 'General Slider'

class Routes(models.Model):
    img = models.ImageField('Image',upload_to='media')
    title1 = models.CharField('Slide Title', max_length=255)
    title2 = models.CharField('Slide Title', max_length=255)
    text = models.TextField('Slide Text')
    
    def __str__(self) -> str:
        return self.title1
    
    class Meta:
        verbose_name = 'Routes'
        verbose_name_plural = 'Routes'

class Pictures(models.Model):
    img = models.ImageField('Image',upload_to='media')
    
    def __str__(self) -> str:
        return 'Text'
    
    class Meta:
        verbose_name = 'Pictures'
        verbose_name_plural = 'Pictures'

class ContactUs(models.Model):
    name = models.CharField('Name',max_length=255)
    email = models.EmailField('Email')
    subject = models.CharField('Subject',max_length=255)
    message = models.TextField('Message')

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

class BlogDate(models.Model):
    date = models.DateField('Blog Date')\
    
    def __str__(self) -> str:
        return self.date.__str__()
    
    class Meta:
        verbose_name = 'Blog Date'
        verbose_name_plural = 'Blog Date'


class Blog(models.Model):
    date = models.ForeignKey(BlogDate, on_delete=models.CASCADE, related_name='blog_date')

    img = models.ImageField('Image',upload_to='media')
    title = models.CharField('Title',max_length=255)
    text = models.TextField('Text')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'






































