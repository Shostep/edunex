from django.db import models
from django.conf import settings

class HostelBlock(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=10, choices=[('male','Male'),('female','Female'),('mixed','Mixed')])
    total_rooms = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'hostel_block'


class HostelRoom(models.Model):
    block = models.ForeignKey(HostelBlock, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField(default=4)
    occupied = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = 'hostel_room'
        unique_together = ['block', 'room_number']

    @property
    def available_beds(self):
        return self.capacity - self.occupied


class HostelAllocation(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    room = models.ForeignKey(HostelRoom, on_delete=models.CASCADE)
    session = models.ForeignKey('academics.Session', on_delete=models.CASCADE)
    allocated_at = models.DateTimeField(auto_now_add=True)
    allocated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'hostel_allocation'
        unique_together = ['student', 'session']
