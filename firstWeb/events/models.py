from django.db import models



class Venue(models.Model):
    name = models.CharField("Full Name", max_length=60)
    email = models.EmailField('Email', max_length=200)
    address = models.CharField('Address', max_length=200)
    owner_phone = models.CharField("Owner's Phone Number", max_length=9)
    client_phone = models.CharField("Client's Phone Number", max_length=9)
    my_date = models.CharField("exact Date", max_length=13)
    my_time = models.CharField("exact Time", max_length=5)

    def __str__(self):
        return self.name + " " + self.address



"""
class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name





class Event(models.Model):
    name = models.CharField('Even Name', max_length=120)
    event_date = models.DateTimeField('Event date')
    manager = models.CharField(max_length=60)
    describtion = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

"""