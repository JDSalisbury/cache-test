from django.test import TestCase
from django.test import tag
from testappmodel.models import Blog
from testappmodel.serializers import BlogSerializer


def create_blog(**params):
    default = {
        "id": 1,
        "name": "First Best Blog",
        "slug": "3323",
        "body": "This is the body of this Blog about stuff."
    }
    default.update(params)

    return Blog.objects.create(**default)


class ViewTests(TestCase):

    @tag('view')
    def test_blogs_view(self):
        response = self.client.get('/api/v1/blogs/', follow=True)
        self.assertEqual(response.status_code, 200)

    @tag('view')
    def test_blog_view(self):
        """ Testing Single Blog View, This needs pk that could change. """
        create_blog()

        res = self.client.get('/api/v1/blog/1/', follow=True)
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        response = self.client.get('/api/v1/blogs/', follow=True)

        print(serializer.data)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(res.status_code, 200)

    @tag('view')
    def test_add_blogs(self):
        """ Testing the Data Drop End point, this actually runs task. """

        res = self.client.get('/api/v1/dataDrop/10/', follow=True)
        print(res.data)
        self.assertEqual(res.status_code, 200)
