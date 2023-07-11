from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=256)


    @property
    def product_count(self):
        return self.category_producty.all().count()


class Producty(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='category_producty')
    rating = models.FloatField(default=0)

    @property
    def filtered_review(self):
        return self.reviews.all()

    @property
    def rating(self):
        count = self.reviews.all().count()
        stars = sum([i.stars for i in self.reviews.all()])
        return stars // count

    @property
    def category_name(self):
        return self.category.name if self.category else " "


STAR_CHOICES = (
    (1, '* '),
    (2, 2 * '* '),
    (3, 3 * '* '),
    (4, 4 * '* '),
    (5, 5 * '* '),
)


class Review(models.Model):
    text = models.TextField()
    producty = models.ForeignKey(Producty, on_delete=models.CASCADE, null=True, related_name='reviews')
    stars = models.IntegerField(default=5, choices=STAR_CHOICES)

    def __str__(self):
        return self.text

