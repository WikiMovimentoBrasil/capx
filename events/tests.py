from django.test import TestCase
from .models import Event

# Create your tests here.

class EventModelTest(TestCase):
    def test_event_creation(self):
        # Test creating an Event instance
        event = Event.objects.create(
            name="Test Event",
            creator=None,
            date_of_creation="2023-10-20",
            date_of_last_edit="2023-10-20",
            description="Test description",
            wiki_link="http://example.com",
            in_person_event=True,
            country="Test Country",
        )

        self.assertEqual(event.name, "Test Event")
        self.assertEqual(event.in_person_event, True)
