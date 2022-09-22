from django.db import models

# Create your models here.

class Article(models.Model):
    a = [('A1', 'A1')]
    b = [('100', '100')]

    c = [('S', 'S-Single Led (Single LED With Single Relay Output)'), 
         ('D', 'D-Dual Led (Trip Relay/Non-Trip Relay without NO/NC)'), 
         ('M', 'M-Dual Led (Trip Relay/Non-Trip Relay with NO/NC)')]

    d = [('00', '00'),('01', '01'),('02', '02'),('03', '03'),('04', '04'),('05', '05'),('06', '06'),('07', '07'),('08', '08'),]
    e = [('4', '4'), ('8', '8'), ('12', '12'), ('16', '16'), ('32', '32'),]
    f = [('X', 'X - Big'), ('Y', 'Y - Small'), ('Z', 'Z - Small & Big')]
    g = [('U', 'U - 80V to 270VAC/DC'), 
         ('D', 'D - 24V to 80V DC')]

    h = [('A', 'A - All Red'), 
         ('B', 'B - Red & Yellow'), 
         ('C', 'C - Red & White'), 
         ('D', 'D - Red & Amber'), 
         ('E', 'E - All White'), 
         ('F', 'F - All Yellow'), 
         ('G', 'G - All Amber'), 
         ('H', 'H - White & Amber'), 
         ('I', 'I - White & Yellow'),]

    i = [('0', '0 - Without DC Fail'), 
         ('1', '1 - With DC Fail(C5 & C6)'), 
         ('2', '2 - Standby Power Supply Only (without DC Fail)')] 

    j = [('12', 'DC Fail Window N'),]
    k = [('0', '0-Without AC Fail'), 
         ('1', '1-With AC Fail -Non-Trip Contacts(C3&C4)'), 
         ('2', '2-With AC Fail -Seperate Contacts (C7 & C8)')]
    l = [('11', 'AC Fail Window'),]

    A = models.CharField(max_length=2, choices=a)
    B = models.CharField(max_length=3, choices=b)
    C = models.CharField(max_length=2, choices=c)
    D = models.CharField(max_length=2, choices=d)
    E = models.CharField(max_length=2, choices=e)
    F = models.CharField(max_length=2, choices=f)
    G = models.CharField(max_length=2, choices=g)
    H = models.CharField(max_length=2, choices=h)
    I = models.CharField(max_length=2, choices=i)
    J = models.CharField(max_length=20, choices=j)
    K = models.CharField(max_length=2, choices=k)
    L = models.CharField(max_length=20, choices=l, null=True)

    def __str__(self):
        return self.A

