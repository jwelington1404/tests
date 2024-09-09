import factory
from faker import Faker
from myapp.models import Product  # Adjust the import to match your app structure

fake = Faker()

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.LazyAttribute(lambda _: fake.word())
    description = factory.LazyAttribute(lambda _: fake.sentence())
    price = factory.LazyAttribute(lambda _: round(fake.pyfloat(left_digits=2, right_digits=2, positive=True), 2))
    stock = factory.LazyAttribute(lambda _: fake.random_int(min=0, max=1000))
    sku = factory.LazyAttribute(lambda _: fake.unique.ean(length=13))
