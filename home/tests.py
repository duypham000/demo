from django.test import TestCase,SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    #các testcase đều cần bắt đầu bằng test_
    def test_homeapp(self):
        # gọi path để lấy response return từ views
        response = self.client.get('')
        # kiểm tra status
        self.assertEquals(response.status_code, 200)