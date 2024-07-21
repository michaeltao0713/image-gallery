import os
from django.core.management.base import BaseCommand
from gallery.models import Images, Changes


class Command(BaseCommand):
    help = "Scan the selected folder for images, update and keep track of conflicts"

    def add_arguments(self, parser):
        parser.add_argument('folder', type=str, help='The folder to scan for images')

    def handle(self, *args, **kwargs):
        # Take in the argument
        folder = kwargs['folder']
        existing_file_paths = set(Images.objects.values_list('file_path', flat=True))
        folder_file_paths = set()

        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
                    file_path = os.path.join(root, file)
                    folder_file_paths.add(file_path)

                    if file_path not in existing_file_paths:
                        # Add new image entry
                        Images.objects.create(title=file, file_path=file_path)
                        self.stdout.write(self.style.SUCCESS(f'Added new image: {file_path}'))
                    else:
                        # File path exists in the database, so log it for review
                        Changes.objects.create(file_path=file_path, change_type='update')
                        self.stdout.write(self.style.WARNING(f'File exists, logged for review: {file_path}'))

        # Check for entries in the database that are not in the folder
        for file_path in existing_file_paths:
            if file_path not in folder_file_paths:
                Changes.objects.create(file_path=file_path, change_type='delete')
                self.stdout.write(self.style.WARNING(f'File missing in folder, logged for review: {file_path}'))

        self.stdout.write(self.style.SUCCESS('Scan complete'))