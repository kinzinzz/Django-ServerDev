from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class LoginUser(models.Model):

    user_id = models.CharField(max_length=20, unique=True, null=False, default=False)
    user_pw = models.CharField(max_length=256, null=False, default=False)    
    
    birth_day = models.DateField(verbose_name="생년월일", null=True)
    gender = models.CharField(verbose_name="성별", max_length=6, null=False, default='male')
    email = models.CharField(verbose_name="이메일 주소", max_length=255, null=False, default=False)
    name = models.CharField(verbose_name="이름", max_length=20, null=False, default=False)
    age = models.IntegerField(verbose_name="나이", default=20)
    # profile_image = ProcessedImageField(upload_to='user_profile_image',
    #                                        processors=[ResizeToFill(100, 50)],
    #                                        format='JPEG',
    #                                        options={'quality': 100}, blank=True)
    

    class Meta:
        db_table = "Login_user"
        verbose_name = "로그인 테스트 테이블"
