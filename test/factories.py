import factory
from factory.fuzzy import FuzzyChoice, FuzzyFloat
from service.models import Product, Category

class ProductFactory(factory.Factory):
    """Creates fake products for testing"""
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("word")
    description = factory.Faker("text")
    price = FuzzyFloat(1.0, 100.0)
    available = FuzzyChoice(choices=[True, False])
    category = FuzzyChoice(
        choices=[
            Category.UNKNOWN,
            Category.CLOTHS,
            Category.FOOD,
            Category.HOUSEWARES,
            Category.AUTOMOTIVE,
            Category.TOOLS,
        ]
    )
