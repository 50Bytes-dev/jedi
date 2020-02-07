from django.contrib import admin
from .models import Jedi, Candidate, Question, Planet, Answer

admin.site.register(Jedi)
admin.site.register(Candidate)
admin.site.register(Question)
admin.site.register(Planet)
admin.site.register(Answer)
