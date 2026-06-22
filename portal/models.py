from django.db import models

class Student(models.Model):

    student_name = models.CharField(max_length=100)
    course_code = models.IntegerField()

    previous_qualification_grade = models.FloatField()
    admission_grade = models.FloatField()

    tuition_fees_up_to_date = models.IntegerField()
    gender = models.IntegerField()
    age_at_enrollment = models.IntegerField()

    scholarship_holder = models.IntegerField()
    debtor = models.IntegerField()

    units_1st_sem_enrolled = models.IntegerField()
    units_1st_sem_approved = models.IntegerField()
    units_1st_sem_grade = models.FloatField()

    units_2nd_sem_enrolled = models.IntegerField()
    units_2nd_sem_approved = models.IntegerField()
    units_2nd_sem_grade = models.FloatField()

    withdrawal_rate = models.FloatField()
    gpa_trend = models.FloatField()
    approval_ratio = models.FloatField()

    attendance_rate = models.FloatField()
    engagement_score = models.FloatField()

    prediction = models.CharField(max_length=50)