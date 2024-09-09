import factory
from myapp.models import Product

class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Product
        sqlalchemy_session = db_session  # Use a sessão do banco de dados para testes

    id = factory.Sequence(lambda n: n)
    name = factory.Faker('word')
    category = factory.Faker('word')
    available = factory.Faker('boolean')
    price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)

def test_product_factory(db_session):
    product = ProductFactory()
    assert product is not None
    assert isinstance(product.name, str)
