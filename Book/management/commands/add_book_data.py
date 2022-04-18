from django.core.management.base import BaseCommand

from  Book.models import Book
class Command(BaseCommand):
    help = "Add data to Book"

    def handle(self, *args, **options):
        Book.objects.create(name="Management command title")