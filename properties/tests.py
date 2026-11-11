from django.test import TestCase
from django.urls import reverse
from accounts.models import User
from .models import Property


# Create your tests here.
class PublicListingTests(TestCase):
    def setUp(self) :
        self.landlord = User.objects.create_user(
            
            username="landlord1",
            password="Strong-test-password-123",
            role=User.Role.LANDLORD,
        )
    def make_property(self, title, status):
        return Property.objects.create(
            landlord=self.landlord,
            title=title,
            description="A test rental property.",
            area="Kiharu",
            property_type=Property.PropertyType.BEDSITTER,
            monthly_rent=5000,
            status=status,
        )
    def test_home_shows_only_approved_properties(self):
        self.make_property("Visible house", Property.Status.APPROVED)
        self.make_property("Hidden house", Property.Status.PENDING)
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Visible house")
        self.assertNotContains(response, "Hidden house")