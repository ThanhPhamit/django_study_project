from django.db import models


class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.menu_category_name


class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(
        MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")

    def __str__(self):
        return self.menu_item
        


class Teacher(models.Model): 
    TeacherID = models.IntegerField(primary_key=True) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50) 
 
class Subject(models.Model): 
    Subjectcode = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=30) 
    credits = models.IntegerField() 
    teacher = models.ManyToManyField(Teacher) 

class Loggeṛ(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="Enter the exact time!")

class Person(models.Model):
    name = models.CharField(max_length=200)
    year_olds = models.IntegerField(default=15)

    def __str__(self) -> str:
        return self.name

# c = MenuCategory.objects.get(pk=1)
# v = Menu.objects.create(menu_item = "menu_item1", price = 15, category_id = c)

# Teacher.objects.create(TeacherID = 1, Qualification = "Intermediate teacher", email = "b@gmail.com")
# sub = Subject(Subjectcode = 5, name = "Mathematic", credits = 1501)
# teacher1 = Teacher.objects.get(TeacherID = 1)
# teacher2 = Teacher.objects.get(TeacherID = 2)
# sub = Subject(Subjectcode = 5, name = "Mathematic", credits = 1501)
# sub.save()
# sub.teacher.add(teacher1)
# sub.teacher.add(teacher2)




