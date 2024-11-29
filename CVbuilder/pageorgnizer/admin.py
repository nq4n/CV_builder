from django.contrib import admin
from .models import CV, WorkExperience

class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 1

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    inlines = [WorkExperienceInline]