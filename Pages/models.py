# from django.db import models

# # class Student(models.Model):
# #     GENDER_CHOICES = [
# #         ('M', 'Male'),
# #         ('F', 'Female'),
# #         ('O', 'Other'),
# #     ]

# #     first_name = models.CharField(max_length=100)
# #     last_name = models.CharField(max_length=100)
# #     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
# #     student_id = models.CharField(max_length=20, unique=True)
# #     enrollment_date = models.DateField()
# #     phone = models.CharField(max_length=15)
# #     status = models.CharField(max_length=50)

# #     def __str__(self):
# #         return f"{self.first_name} {self.last_name}"

# class Teacher(models.Model):
#     name = models.CharField(max_length=100)
#     teacher_id = models.CharField(max_length=20, unique=True)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)

#     def __str__(self):
#         return self.name

# class Course(models.Model):
#     course_id = models.CharField(max_length=20, unique=True)
#     course_name = models.CharField(max_length=200)
#     description = models.TextField()
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

#     def __str__(self):
#         return self.course_name

# class Class(models.Model):
#     class_id = models.CharField(max_length=20, unique=True)
#     name = models.CharField(max_length=100)
#     room = models.CharField(max_length=50)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='classes')

#     def __str__(self):
#         return self.name

# class Attendance(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
#     class_session = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='attendances')
#     date = models.DateField()
#     status = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.student} - {self.class_session} - {self.date}"

# # class Certificate(models.Model):
# #     GRADE_CHOICES = [
# #         ('TB', 'Très Bien'),
# #         ('B', 'Bien'),
# #         ('AB', 'Assez Bien'),
# #         ('P', 'Passable'),
# #     ]

# #     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='certificates')
# #     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certificates')
# #     grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
# #     issued_date = models.DateField()

# #     def __str__(self):
# #         return f"{self.student} - {self.course} - {self.grade}"
