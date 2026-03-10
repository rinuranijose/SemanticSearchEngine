import csv
import os
import sys
from django.conf import settings
from django.core.management.base import BaseCommand
from project.models import Document
from project.services import get_embedding


class Command(BaseCommand):

    help = "Ingest documents with embeddings"

    def handle(self, *args, **kwargs):
        file_path = r"C:\Users\USER\PycharmProjects\SemanticSearchEngine\data\documents.csv"
        with open(file_path) as f:

            reader = csv.DictReader(f)

            for row in reader:

                title = row["title"]
                content = row["content"]

                embedding = get_embedding(content)
                Document.objects.create(
                    title=title,
                    content=content,
                    embedding=embedding
                )

        print("Documents ingested successfully")