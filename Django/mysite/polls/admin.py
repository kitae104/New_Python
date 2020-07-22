from django.contrib import admin

# 사용자가 작성한 모델 등록을 여기에...

from polls.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)






