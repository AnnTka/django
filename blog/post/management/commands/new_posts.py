from django.core.management.base import BaseCommand
from django.conf import settings
from post.models import Post
import csv


class Command(BaseCommand):
    help = "Uploaded posts from DB"

    def handle(self, *args, **options):
        with open(settings.BASE_DIR / "posts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                Post.objects.create(title=row[0], slug=row[1], text=row[2])
