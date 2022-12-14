from django.contrib import admin
from .models import Answer, Comment, Question


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    search_fields = ('title', 'detail')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('answer', 'comment')


admin.site.register(Comment, CommentAdmin)
