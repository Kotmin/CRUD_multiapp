from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    class Status(models.TextChoices): #alt IntegerChoices
        ACT = "1","Active"
        COMPL = "2","Completed"
        SUS = "3","Suspended"
        DEL = "0","Deleted"
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True) #One to many relation
    # on_delete - set action to all inherited tasks after user deletion, 
    # CASCADE - deletes all tasks
    # SET_NULL - set null to this field for all tasks
    # DO_NOTHING - my fav <3

    # null = True, blank =True. Allow to leave this fieldt empty in database.
    #  Can be null? Yas. Have we to change it later? Yass
    title = models.CharField(max_length=200, null=True,blank=True)
    description = models.TextField(null=True,blank=True)# that's also good for forms
    state = models.CharField(max_length=2,
                            choices=Status.choices,
                            default=Status.ACT
                            )
    create_date = models.DateTimeField(auto_now_add=True)

    # Auto generated str overload
    # def __str__(self) -> str:
    #     return super().__str__()

    def __str__(self):
        return self.title

    