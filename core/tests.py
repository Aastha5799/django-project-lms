from django.test import TestCase

from core.models import Teacher
from django.contrib.auth.models import User
# Create your tests here.
class TeacherModelTest(TestCase):

    def test_teacher_model_creation(self):
        #case one:user exists
        teacher= Teacher.objects.create(
            full_name="Hiraman Chaudary",
            email="hiraman@gmail.com",
            department="BCA",
            phone_number=980000000,
            join_date='2025-02-02',
            user=User.objects.create_user(username="testuser",password="21we21@@")
        )
        try:
            #case one:user exists
            print("case 1:user exists with same username")
            self.assertEqual(teacher.full_name,"Hiraman Chaudary")
            self.assertEqual(teacher.email,"hiraman@gmail.com")
            self.assertEqual(teacher.department,"BCA")
            self.assertEqual(teacher.phone_number,980000000)
            self.assertEqual(teacher.join_date,'2025-02-02')
            self.assertEqual(teacher.user,User.objects.get(username="testuser")) #same user
            print("case 1:user exists with same username passed")
        except Exception as e:
            print("error:",e)

        try:
            #case two:user exists
            print("case 2:user exists with different username")
            self.assertEqual(teacher.full_name,"Hiraman Chaudary")
            self.assertEqual(teacher.email,"hiraman@gmail.com")
            self.assertEqual(teacher.department,"BCA")
            self.assertEqual(teacher.phone_number,980000000)
            self.assertEqual(teacher.join_date,'2025-02-02')
            self.assertEqual(teacher.user,User.objects.get(username="disha")) #same user
        except Exception as e:
            print("error:",e)
            print("error:","User must be same for teacher.")

        #case three:phone number length
            print("case 3:phone number length")
            self.assertEqual(teacher.full_name,"Hiraman Chaudary")
            self.assertEqual(teacher.email,"hiraman@gmail.com")
            self.assertEqual(teacher.department,"BCA")
            self.assertEqual(teacher.phone_number,9800000000) #phone number length is 9 but passing 10
            self.assertEqual(teacher.join_date,'2025-02-02')
            self.assertEqual(teacher.user,User.objects.get(username="disha")) #same user
        except Exception as e:
            print("error:",e)
            print("error:","required phone number length is 9")

    def test_teacher_model_email_exist(self):
        #case one:user exists
        teacher= Teacher.objects.create(
            full_name="KP Oli",
            email="kpoli@gmail.com",
            department="BCA",
            phone_number=980000000,
            join_date='2025-02-02',
            user=User.objects.create_user(username="testemail",password="21we21@@")
        )

        #case 1:email different
        try:
            #case two:user with different email
            print("case email:email  different ")
            self.assertEqual(teacher.full_name,"KP Oli")
            self.assertEqual(teacher.email,"hiraman@gmail.com")
            self.assertEqual(teacher.department,"BCA")
            self.assertEqual(teacher.phone_number,980000000)
            self.assertEqual(teacher.join_date,'2025-02-02')
            self.assertEqual(teacher.user,User.objects.get(username="testemail")) #same user
        except Exception as e:
            print("error:",e)
            print("error:"," email already available")