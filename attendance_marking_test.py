"""AttendX attendance-marking automation test (SIMULATED).

This file does NOT connect to a real AttendX application. It uses an
in-memory FakeAttendanceService to demonstrate marking attendance,
verifying recorded status, and rejecting duplicate marking.

Run:  python attendance_marking_test.py -v
"""
import unittest


class DuplicateAttendanceError(Exception):
    """Raised when attendance is already marked for a student on a date."""


class FakeAttendanceService:
    """Simulated AttendX attendance backend (one record per student per date)."""

    VALID_STATUSES = {"Present", "Absent"}

    def __init__(self):
        self._records = {}

    def mark_attendance(self, student_id, date, status):
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status: {status}")
        key = (student_id, date)
        if key in self._records:
            raise DuplicateAttendanceError(f"Attendance already marked for {student_id} on {date}")
        self._records[key] = status

    def get_status(self, student_id, date):
        return self._records.get((student_id, date))


class AttendanceMarkingTest(unittest.TestCase):
    def setUp(self):
        self.service = FakeAttendanceService()

    def test_mark_student_present_is_recorded(self):
        self.service.mark_attendance("S101", "2026-10-17", "Present")
        self.assertEqual(self.service.get_status("S101", "2026-10-17"), "Present")

    def test_mark_student_absent_is_recorded(self):
        self.service.mark_attendance("S102", "2026-10-17", "Absent")
        self.assertEqual(self.service.get_status("S102", "2026-10-17"), "Absent")

    def test_unmarked_student_has_no_record(self):
        self.assertIsNone(self.service.get_status("S103", "2026-10-17"))

    def test_duplicate_attendance_is_rejected_and_original_kept(self):
        self.service.mark_attendance("S101", "2026-10-17", "Present")
        with self.assertRaises(DuplicateAttendanceError):
            self.service.mark_attendance("S101", "2026-10-17", "Absent")
        self.assertEqual(self.service.get_status("S101", "2026-10-17"), "Present")

    def test_invalid_status_is_rejected(self):
        with self.assertRaises(ValueError):
            self.service.mark_attendance("S101", "2026-10-17", "Maybe")


if __name__ == "__main__":
    unittest.main()
