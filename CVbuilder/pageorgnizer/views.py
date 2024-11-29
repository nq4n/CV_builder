from django.shortcuts import render , HttpResponse , redirect
from .models import CV, WorkExperience

def home(request):
    return render(request , 'home.html' )
def profile(request):
    return render(request , 'profile.html')
def cv_made(request):
    return render(request , 'CV_builder.html')
def cv_viwer(request):
    return render(request , 'cv_viwer')

#python manage.py makemigrations
#python manage.py migrate
def save_cv(request):
    if request.method == "POST":
        # Personal Information
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        photo = request.FILES.get("photo")

        # Education Information
        degree = request.POST.get("degree")
        university = request.POST.get("university")
        graduation_year = request.POST.get("graduation_year")

        # Skills
        skills = request.POST.get("skills")

        # Save CV Data
        cv = CV.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            photo=photo,
            degree=degree,
            university=university,
            graduation_year=graduation_year,
            skills=skills
        )

        # Work Experience (Loop through all submitted experiences)
        experience_count = 1
        while f"job_title_{experience_count}" in request.POST:
            job_title = request.POST.get(f"job_title_{experience_count}")
            company = request.POST.get(f"company_{experience_count}")
            years_worked = request.POST.get(f"years_worked_{experience_count}")

            if job_title and company and years_worked:
                WorkExperience.objects.create(
                    cv=cv,
                    job_title=job_title,
                    company=company,
                    years_worked=years_worked
                )
            experience_count += 1

        # Redirect to a success page or render a success message
        return redirect('success')

    return render(request, 'cv_form.html')
