from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User






class Member(models.Model):

    SURBUBS = (
        ('Kuyasa', 'Kuyasa'), ('Harare', 'Harare'), ('Makhaza', 'Makhaza'), ('Site B', 'Site B'), ('Site C', 'Site C'),('kraaifontain', 'Kraaifontain')
        
    )
    CHOICES= (('paid' ,'paid'), ('pending', 'pending'))
    First_Name    = models.CharField(max_length=20)
    Last_Name     = models.CharField(max_length=20)
    Cell_Number   = models.CharField(max_length=10 )
    Surbub        = models.CharField(max_length=200, choices=SURBUBS)
    admin         = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Date          = models.DateTimeField(auto_now_add=True)
      

    def __str__(self):
        return "%s %s " % (self.Last_Name, self.First_Name)

    class Meta:
        unique_together =[ ['Last_Name', 'First_Name' ]  ]   
        ordering        = ('-Date',)
                 

class Deceased(models.Model):
    Name       = models.ForeignKey(Member, default=False, related_name='deceased_name_set', on_delete=models.CASCADE)
    Date_Deceased    = models.DateTimeField(auto_now_add=True, null=True)
 
    def __str__(self):
        return str(self.Name)


class Contributions(models.Model):
    Paid= (('not_paid','not_paid'),('paid','paid'))

    deceased          = models.ForeignKey(Deceased, default=True, on_delete=models.CASCADE, related_name= '+')
    Name              = models.OneToOneField(Member, default=True, on_delete=models.CASCADE)
    admin             = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name= '+')
    Date              = models.DateTimeField(auto_now_add=True, null=True)

   
    def __str__(self): 
        return str(self.Name)       
     
    class Meta:
        unique_together =[ ['deceased', 'Name' ]  ] 
        ordering        = ('-Date', 'Name')   


