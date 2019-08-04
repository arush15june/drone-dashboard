import unittest
from unittest.mock import patch

from models import DroneState
import drones
from db import in_memory_db, db_session
from main import app

class baseTestCase(unittest.TestCase):
    """ base class to setup project. """
    def setUp(self):
        self.app = app
        self.client = app.test_client()
        self.session = in_memory_db()
        db_session = self.session
        DroneState.query = self.session.query_property()
        self._populate_test_data()

    def _populate_test_data(self):
        for i in range(10):
            d = DroneState(uuid=i)
            self.session.add(d)
            self.session.commit()

class testApiClass(baseTestCase):
    """ Tests for API class. """
    
    def test_get_all_drones(self):
        r = self.client.get('/api/drones')
        self.assertEqual(r.status_code, 200)

    def test_single_drone(self):
        r = self.client.get('/api/drones/1')
        self.assertEqual(r.status_code, 200)

    def test_add_drone(self):
        r = self.client.post('/api/drones', json={})
        self.assertEqual(r.status_code, 201)

class testDronesClass(baseTestCase):
    """ tests for module drones. """
    
    def test_get_drone_uuid(self):
        drone = drones.get_drone_uuid(1)
        self.assertEqual(drone['uuid'], '1')

    def test_get_all_drones(self):
        all_drones = drones.get_all_drones()
        self.assertEqual(all_drones[0]['uuid'], '0')

    def test_serialize_drone_state(self):
        drone = DroneState.query.get('1')
        self.assertEqual(drones.serialize_drone_state(drone).data['uuid'], '1')
    
if __name__ == "__main__":
    unittest.main()