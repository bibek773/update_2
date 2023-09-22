from django.contrib import admin
from authentication.models import Userinfo

# Register your models here.

class UserInfo(admin.ModelAdmin):
    list_display =('id','userinfo_name','userinfo_Uname','userinfo_Ftname','userinfo_Mtname','userinfo_email','userinfo_userpic','userinfo_phoneno1','userinfo_phoneno2','userinfo_phoneno3','userinfo_password','userinfo_password','userinfo_gender','userinfo_Edulvl','userinfo_Expedu','userinfo_State','userinfo_City','userinfo_Zip','userinfo_DoB','userinfo_jdate')



admin.site.register(Userinfo)