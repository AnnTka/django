from django.core.management.base import BaseCommand
from django.conf import settings
from post.models import Post
import csv


class Command(BaseCommand):
    help = "Show all posts from DB"

    def handle(self, *args, **options):
        with open(settings.BASE_DIR / "posts.csv", "w") as file:
            writer = csv.writer(file)
            for post in Post.objects.all():
                writer.writerow([post.title, post.slug, post.text])
