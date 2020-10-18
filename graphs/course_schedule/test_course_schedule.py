from unittest import TestCase
from course_schedule import course_schedule

class CourseScheduleTest(TestCase):

    def test_01_course_schedule(self):
        p = [[1,0]]
        N = 2
        self.assertEqual(course_schedule(N, p), True)

    def test_02_course_schedule(self):
        p = [[1,0],[0,1]]
        N = 2
        self.assertEqual(course_schedule(N, p), False)

    def test_03_course_schedule(self):
        N = 4
        p = [[2,0],[1,0],[3,1],[3,2],[1,3]]
        self.assertEqual(course_schedule(N, p), False)

    def test_04_course_schedule(self):
        N = 5
        p = [[0,1],[1,2],[1,3],[2,4],[4,3]]
        self.assertEqual(course_schedule(N, p), True)