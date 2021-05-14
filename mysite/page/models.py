from django.db import models

import uuid
import random

def random_integer():
    return int(random.randint(0, 4))

# Create your models here.
class Attempt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_id = models.CharField(max_length=50)
    random_id = models.IntegerField(default = random_integer)