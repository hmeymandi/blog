from django.test import TestCase
from django.shortcuts import reverse
from blog.models import Post
from django.contrib.auth.models import User



class BlogTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user')
        self.post1 = Post.objects.create(
            title= "Test 1",
            text = "this is a test text",
            
            status=Post.STATUS_CHOICES[0],
            author = self.user,  
        )
    

    def test_post_listview_url(self) :
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_listview_url_by_name(self) :
        response = self.client.get(reverse('post_listview'))
        self.assertEqual(response.status_code,200)

    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse("post_listview"))
        self.assertContains(response,self.post1.title)

    def test_post_detail(self):
        response = self.client.get(
            reverse('post_detail_view', kwargs={'pk': self.post1.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_post_list_template(self):
        response = self.client.get(reverse('post_listview'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')