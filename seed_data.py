# initialize environment
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jangocam.settings')

import django
django.setup()

# Fake data seed script
from faker import Faker
from links.models import Link

seed_fake = Faker()

# Link
#   - url
#   - description

def create_links():
    fake_url = seed_fake.url()
    fake_description = seed_fake.sentences(nb=3)
    link = Link.objects.get_or_create(url=fake_url, description=fake_description)[0]
    # get_or_create return tuple hence [0]
    link.save()

def generate_links(n = 20):
    for item in range(n):
        create_links()

if __name__ == '__main__':
    generate_links()

