from mqtt_conection import *
from preconditions import *
import unittest


class TestPermitJoin(unittest.TestCase):

    correlationId = get_random_correlationId()
    userId = get_random_userId()
    hubId = "raspberrypi"

    def test_permit_join_enable(self):
        command = {
            "_commandType": "PermitJoinEnableCommand",
            "_correlationId": self.correlationId,
            "_userId": self.userId,
            "_id": self.hubId
        }

        event = send(command)

        expected_event = {
            "_id": self.hubId,
            "_correlationId": self.correlationId,
            "_userId": self.userId,
            "_eventType": "PermitJoinEnabled",
            "timeout": 60
        }

        self.assertEqual(expected_event, event, "JSON (test_permit_join_enable) does not match")

    def test_permit_join_disable(self):
        command = {
            "_commandType": "PermitJoinDisableCommand",
            "_correlationId": self.correlationId,
            "_userId": self.userId,
            "_id": self.hubId
        }

        event = send(command)

        expected_event = {
            "_id": self.hubId,
            "_correlationId": self.correlationId,
            "_userId": self.userId,
            "_eventType": "PermitJoinDisabled"
        }

        self.assertEqual(expected_event, event, "JSON (test_permit_join_disable) does not match")


if __name__ == '__main__':
    unittest.main()