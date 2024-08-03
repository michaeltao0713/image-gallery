from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Images Model - Stores file location and metadata
class Images(models.Model):
    # Title of the image
    title = models.CharField(max_length=100)
    # File Path of the image - Should be unique
    file_path = models.CharField(max_length=256, null=True)
    # Creates a through table for a "many to many" relationship between Tags and Images
    tags = models.ManyToManyField(Tags, related_name='images', blank=True)

    # Return title of image
    def __str__(self):
        return self.title


# Changes Model - Stores changes between target folder and Images table
class Changes(models.Model):
    # File Path of the image - Should be unique
    file_path = models.CharField(max_length=256, null=True)
    # Type of change/discreptancy between the table and the folder
    change_type = models.CharField(max_length=50)

    # Returns file path and reason why it was flagged
    def __str__(self):
        return f"{self.file_path} - {self.change_type}"
