from django.shortcuts import render, redirect
import joblib
import pandas as pd
from .models import Student

model = joblib.load('portal/model.joblib')
encoders = joblib.load('portal/encoders.joblib')
from django.shortcuts import render, redirect

def login(request):
    return render(request, 'login.html')

def student(request):

    if request.method == "POST":

        data = {
            "course_code": float(request.POST.get('course_code')),
            "previous_qualification_grade": float(request.POST.get('previous_qualification_grade')),
            "admission_grade": float(request.POST.get('admission_grade')),
            "tuition_fees_up_to_date": int(request.POST.get('tuition_fees_up_to_date')),
            "gender": int(request.POST.get('gender')),
            "age_at_enrollment": int(request.POST.get('age_at_enrollment')),
            "scholarship_holder": int(request.POST.get('scholarship_holder')),
            "debtor": int(request.POST.get('debtor')),
            "units_1st_sem_enrolled": int(request.POST.get('units_1st_sem_enrolled')),
            "units_1st_sem_approved": int(request.POST.get('units_1st_sem_approved')),
            "units_1st_sem_grade": float(request.POST.get('units_1st_sem_grade')),
            "units_2nd_sem_enrolled": int(request.POST.get('units_2nd_sem_enrolled')),
            "units_2nd_sem_approved": int(request.POST.get('units_2nd_sem_approved')),
            "units_2nd_sem_grade": float(request.POST.get('units_2nd_sem_grade')),
            "withdrawal_rate": float(request.POST.get('withdrawal_rate')),
            "gpa_trend": float(request.POST.get('gpa_trend')),
            "approval_ratio": float(request.POST.get('approval_ratio')),
            "attendance_rate": float(request.POST.get('attendance_rate')),
            "engagement_score": float(request.POST.get('engagement_score'))
        }

        sample_df = pd.DataFrame([data])

        prediction = model.predict(sample_df)

        result = encoders["target"].inverse_transform(prediction)[0]

        print("Prediction:", result)
        Student.objects.create(

    student_name=request.POST.get('student_name'),
    course_code=request.POST.get('course_code'),

    previous_qualification_grade=request.POST.get('previous_qualification_grade'),
    admission_grade=request.POST.get('admission_grade'),

    tuition_fees_up_to_date=request.POST.get('tuition_fees_up_to_date'),
    gender=request.POST.get('gender'),
    age_at_enrollment=request.POST.get('age_at_enrollment'),

    scholarship_holder=request.POST.get('scholarship_holder'),
    debtor=request.POST.get('debtor'),

    units_1st_sem_enrolled=request.POST.get('units_1st_sem_enrolled'),
    units_1st_sem_approved=request.POST.get('units_1st_sem_approved'),
    units_1st_sem_grade=request.POST.get('units_1st_sem_grade'),

    units_2nd_sem_enrolled=request.POST.get('units_2nd_sem_enrolled'),
    units_2nd_sem_approved=request.POST.get('units_2nd_sem_approved'),
    units_2nd_sem_grade=request.POST.get('units_2nd_sem_grade'),

    withdrawal_rate=request.POST.get('withdrawal_rate'),
    gpa_trend=request.POST.get('gpa_trend'),
    approval_ratio=request.POST.get('approval_ratio'),

    attendance_rate=request.POST.get('attendance_rate'),
    engagement_score=request.POST.get('engagement_score'),

    prediction=result
)
        

    return render(request, 'student.html', {
    'message': 'Data submitted successfully'
    })
    


def admin_dashboard(request):

    students = Student.objects.all()

    return render(
        request,
        'admin_dashboard.html',
        {'students': students}
    )