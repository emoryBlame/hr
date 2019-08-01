from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Category {}".format(self.title)


class Vacancy(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_starts = models.DateTimeField(auto_now=True)
    date_ends = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Vacancy {}, in Category {}".format(
                    self.title,
                    self.category.title
                )

