from django.db import models


# Images Model - Stores file location and metadata
class Images(models.Model):
    # Title of the image
    title = models.CharField(max_length=100)
    # File path to the image in storage
    # file_path = models.CharField(max_length=256, null=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    # Time image was uploaded to gallery
    upload_time = models.DateTimeField(auto_now_add=True)

    # Return title of image
    def __str__(self):
        return self.title
