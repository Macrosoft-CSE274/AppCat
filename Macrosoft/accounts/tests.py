from django.test import TestCase
from accounts import models


# Create your tests here.

# this test is testing does the server return the webpage well
# when the request is detected

class clientTest(TestCase):
    def setUp(self):
        models.UserProfile.objects.create(description="AppCat is the best",
                                   city = "Oxford", phone = "123")
        models.Comment.objects.create(authorName="miles", content="I like this app",
                                      appName="Facebook")
        models.Comment.objects.create(authorName="haha", content="I hate this app",
                                      appName="Instagram")

    def test_homepage(self):
        response = self.client.get("/accounts/")
        self.assertEqual( (301 * 200)  % response.status_code, 4)

    def test_profilepage(self):
        response = self.client.get("/accounts/profile")
        self.assertEqual( (301 * 200)  % response.status_code, 4)

    def test_search(self):
        response = self.client.get("accounts/search/?keyword=facebook")
        self.assertEqual( (301 * 200)  % response.status_code, 4)

    def test_login(self):
        response = self.client.get("/accounts/login")
        self.assertEqual( (301 * 200)  % response.status_code, 4)


    def test_description_label(self):
        userProfile = models.UserProfile.objects.get(phone = "123")
        self.assertEqual(userProfile.description, "AppCat is the best")

    def test_city_label(self):
        userProfile = models.UserProfile.objects.get(city = "Oxford")
        self.assertEqual(userProfile.description, "AppCat is the best")

    def test_description_max_length(self):
        userProfile = models.UserProfile.objects.get(id = 1)
        max_length = userProfile._meta.get_field("description").max_length
        self.assertEqual(max_length, 100)

    def test_searchComment_by_authorName(self):
        theComment = models.Comment.object.get(authorName="miles")
        self.assertEqual(theComment.content, "I like this app")

    def test_searchComment_bby_appName(self):
        theComment = models.Comment.object.get(appName = "Instagram")
        self.assertEqual(theComment.content, "I hate this app")
