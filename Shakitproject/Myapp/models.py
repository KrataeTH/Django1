from django.db import models

# Create your models here.
from django.db import models

# กำหนด Enum สำหรับประเภทลูกค้า
class CustomerType(models.TextChoices):
    เทศบาลเมือง = 'เทศบาลเมือง'
    เทศบาลตำบล = 'เทศบาลตำบล'
    องค์กรบริหารส่วนตำบล ='องค์กรบริหารส่วนตำบล'
    องค์การบริหารส่วนจังหวัด = 'องค์การบริหารส่วนจังหวัด'

# กำหนด Enum สำหรับสถานะลูกค้า
class CustomerStatus(models.TextChoices):
    ACTIVE = 'Active', 'Active'
    NOT_ACTIVE = 'Not Active', 'Not Active'

class Customer(models.Model):
    # ชื่อลูกค้า
    name = models.CharField(max_length=200)
    
    # ประเภทลูกค้า
    customer_type = models.CharField(
        max_length=100,
        choices=CustomerType.choices,

    )
    
    # ที่อยู่ลูกค้า
    address = models.TextField()
    
    # เบอร์โทรลูกค้า
    phone_number = models.CharField(max_length=15)
    
    # สถานะลูกค้า
    status = models.CharField(
        max_length=10,
        choices=CustomerStatus.choices,
        default=CustomerStatus.ACTIVE,
    )

    def __str__(self):
        return f"{self.name} - {self.customer_type} ({self.status})"

    