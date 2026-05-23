from django.db import models
from django.conf import settings

class ExamTimetable(models.Model):
    course = models.ForeignKey('academics.Course', on_delete=models.CASCADE)
    semester = models.ForeignKey('academics.Semester', on_delete=models.CASCADE)
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.CharField(max_length=200)
    invigilator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        limit_choices_to={'role': 'lecturer'}
    )
    max_capacity = models.PositiveIntegerField(default=100)

    class Meta:
        db_table = 'examination_timetable'
        unique_together = ['course', 'semester']


class ExamClearance(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    semester = models.ForeignKey('academics.Semester', on_delete=models.CASCADE)

    fees_paid = models.BooleanField(default=False)
    courses_registered = models.BooleanField(default=False)
    no_disciplinary_hold = models.BooleanField(default=True)
    library_cleared = models.BooleanField(default=False)
    hostel_cleared = models.BooleanField(default=False)

    is_cleared = models.BooleanField(default=False)
    cleared_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'examination_clearance'
        unique_together = ['student', 'semester']
