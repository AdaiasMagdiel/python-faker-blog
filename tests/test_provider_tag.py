from faker import Faker
from faker_blog import BlogProvider
from faker_blog.utils import slugify

fake = Faker()
fake.add_provider(BlogProvider)


def test_provider_has_tag_method():
    assert hasattr(fake, "article_tag")


def test_provider_tag_is_a_string():
    assert isinstance(fake.article_tag(), str)


def test_provider_has_tag_and_slug_method():
    assert hasattr(fake, "article_tag_and_slug")


def test_provider_tag_and_slug_is_a_dict():
    assert isinstance(fake.article_tag_and_slug(), dict)


def test_slugify_can_slugify_tag():
    data = fake.article_tag_and_slug()

    assert data["slug"] == slugify(data["tag"])
