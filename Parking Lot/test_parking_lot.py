import unittest
from Parking_Lot import Parking


class TestParkingLot(unittest.TestCase):

    def test_create_parking_lot(self):
        parkingLot = Parking()
        Result = parkingLot.Create_New_Slot(6)
        self.assertEqual(6, Result)

    def test_park(self):
        parkingLot = Parking()
        Result = parkingLot.Create_New_Slot(6)
        Result = parkingLot.park("KA-01-HH-1234", "White")
        self.assertNotEqual(-1, Result)

    def test_leave(self):
        parkingLot = Parking()
        Result = parkingLot.Create_New_Slot(6)
        Result = parkingLot.park("KA-01-HH-1234", "White")
        Result = parkingLot.leave(1)
        self.assertEqual(True, Result)

    def test_getRegNoFromColor(self):
        parkingLot = Parking()
        Result = parkingLot.Create_New_Slot(6)
        Result = parkingLot.park("KA-01-HH-1234", "White")
        Result = parkingLot.park("KA-01-HH-9999", "White")
        regnos = parkingLot.getRegNoFromColor("White")
        self.assertIn("KA-01-HH-1234", regnos)
        self.assertIn("KA-01-HH-9999", regnos)

    def test_getSlotNoFromRegNo(self):
        parkingLot = Parking()
        Result = parkingLot.Create_New_Slot(6)
        Result = parkingLot.park("KA-01-HH-1234", "White")
        Result = parkingLot.park("KA-01-HH-9999", "White")
        slotno = parkingLot.getSlotNoFromRegNo("KA-01-HH-9999")
        self.assertEqual(2, slotno)

    def test_getSlotNoFromColor(self):
        parkingLot = Parking()
        Result = parkingLot.Create_New_Slot(6)
        Result = parkingLot.park("KA-01-HH-1234", "White")
        Result = parkingLot.park("KA-01-HH-9999", "White")
        slotnos = parkingLot.getSlotNoFromColor("White")
        self.assertIn("1", slotnos)
        self.assertIn("2", slotnos)


if __name__ == '__main__':
    unittest.main()
