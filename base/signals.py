# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
# from .models import Course, Enrollment

# @receiver(m2m_changed, sender=Course.students.through)
# def add_students_to_enrollment(sender, instance, action, pk_set, **kwargs):
#     if action == 'post_add' or action == 'post_remove':
#         students = instance.students.all()
#         enrollments = Enrollment.objects.filter(course=instance)
#         for enrollment in enrollments:
#             if enrollment.student not in students:
#                 enrollment.delete()
#         for student_id in pk_set:
#             Enrollment.objects.get_or_create(student_id=student_id, course=instance)
