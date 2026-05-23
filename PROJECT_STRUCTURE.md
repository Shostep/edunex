# EduNex Project Structure

edunex/
├── .env.example
├── .gitignore
├── README.md
├── apps/
│   ├── academics/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── accounts/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── signals.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── admission/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   └── views.py
│   ├── alumni/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── admin_custom.py
│   │   ├── context_processors.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   └── views.py
│   ├── examination/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── finance/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── hostel/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── indigene/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── lecturers/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── library/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── medical/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── notifications/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   └── views.py
│   ├── payments/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── paystack.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── setup_wizard/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   └── students/
│       ├── __init__.py
│       ├── admin.py
│       ├── models.py
│       ├── urls.py
│       └── views.py
├── build.sh
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media/
├── render.yaml
├── requirements.txt
├── static/
│   ├── css/
│   │   ├── admin.css
│   │   ├── main.css
│   │   └── responsive.css
│   ├── images/
│   └── js/
│       ├── attendance.js
│       ├── main.js
│       ├── payment.js
│       └── validation.js
├── templates/
│   ├── admission/
│   │   ├── home.html
│   │   ├── pay_acceptance.html
│   │   ├── public_list.html
│   │   ├── respond.html
│   │   ├── start.html
│   │   ├── step_academic.html
│   │   ├── step_payment.html
│   │   ├── step_personal.html
│   │   ├── step_upload.html
│   │   ├── tracker.html
│   │   └── verify.html
│   ├── alumni_portal/
│   │   ├── certificate.html
│   │   ├── dashboard.html
│   │   └── transcript.html
│   ├── base/
│   │   ├── base.html
│   │   ├── base_admin.html
│   │   └── base_auth.html
│   ├── base.html
│   ├── base_admin.html
│   ├── base_auth.html
│   ├── bursar/
│   │   ├── dashboard.html
│   │   ├── fee_structure.html
│   │   ├── payments.html
│   │   ├── receipts.html
│   │   └── reports.html
│   ├── hod/
│   │   ├── dashboard.html
│   │   ├── reports.html
│   │   ├── results_review.html
│   │   └── subjects.html
│   ├── hostel_admin/
│   │   ├── allocations.html
│   │   ├── dashboard.html
│   │   └── rooms.html
│   ├── indigene/
│   │   ├── apply.html
│   │   ├── home.html
│   │   ├── status.html
│   │   ├── tracker.html
│   │   └── upload.html
│   ├── lecturers/
│   │   ├── attendance.html
│   │   ├── ca_entry.html
│   │   ├── courses.html
│   │   ├── dashboard.html
│   │   ├── exam_entry.html
│   │   └── performance.html
│   ├── librarian/
│   │   ├── catalog.html
│   │   ├── dashboard.html
│   │   ├── issue.html
│   │   └── returns.html
│   ├── medical_officer/
│   │   ├── appointments.html
│   │   ├── dashboard.html
│   │   └── records.html
│   ├── registrar/
│   │   ├── admission_list.html
│   │   ├── dashboard.html
│   │   ├── records.html
│   │   ├── screening.html
│   │   └── sessions.html
│   ├── registration/
│   │   ├── login.html
│   │   └── password_reset.html
│   ├── setup/
│   │   ├── review.html
│   │   ├── step_1.html
│   │   ├── step_2.html
│   │   ├── step_3.html
│   │   ├── step_4.html
│   │   ├── step_5.html
│   │   ├── step_6.html
│   │   └── step_7.html
│   └── students/
│       ├── course_reg.html
│       ├── dashboard.html
│       ├── fees.html
│       ├── hostel.html
│       ├── id_card.html
│       ├── library.html
│       ├── medical.html
│       ├── profile.html
│       ├── results.html
│       ├── timetable.html
│       └── transcript.html
└── wsgi_pythonanywhere.py

## Apps Overview

| App | Purpose |
|-----|---------|
| **accounts** | Custom User model with roles |
| **core** | University config, activity logs, notifications |
| **setup_wizard** | No-code university setup (7 steps) |
| **academics** | Faculties, departments, programmes, courses, sessions |
| **indigene** | Indigene verification portal |
| **admission** | E-Screening admission flow |
| **students** | Student portal (registration, results, fees, etc.) |
| **lecturers** | Lecturer portal (attendance, CA, exam entry) |
| **examination** | Exam timetable, clearance |
| **finance** | Fee structure, payments, bursar reports |
| **hostel** | Room management, student allocation |
| **medical** | Health records, appointments |
| **library** | Book catalog, issue/return |
| **alumni** | Post-graduation portal, certificate verification |
| **payments** | Paystack integration |
| **notifications** | Email/SMS/push notification logs |

## Deployment

### Render (Primary)
1. Push to GitHub
2. Connect to Render
3. Add environment variables
4. Auto-deploy

### PythonAnywhere (Secondary)
1. Upload files
2. Configure WSGI (see wsgi_pythonanywhere.py)
3. Set static files path
4. Run migrations
5. Reload

## Setup
First visit redirects to `/setup/` for no-code configuration.
