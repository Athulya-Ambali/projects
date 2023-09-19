from django.db import models


class Coursetb(models.Model):
    course=models.CharField(max_length=30)
    c_id=models.AutoField(primary_key=True)

    # class meta:
    #     verbose_name_plural="Course"
    # def _str_(self):
    #         return self.course

class Syllabustb(models.Model):
    syllabus=models.CharField(max_length=30,unique=True)
    s_id=models.AutoField(primary_key=True)

    # class meta:
    #     verbose_name_plural="Syllabus"
    # def _str_(self):
    #         return self.syllabus