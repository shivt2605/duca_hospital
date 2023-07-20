# Generated by Django 4.2.3 on 2023-07-18 08:25

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('license_no', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact_no', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('medicine_details', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('prescription', models.FileField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('department', models.CharField(choices=[('Physician', 'Physician'), ('Orthopedic', 'Orthopedic'), ('Gynecology', 'Gynecology'), ('Pediatric', 'Pediatric'), ('Cardiologist', 'Cardiologist'), ('Dental', 'Dental'), ('ENT', 'ENT'), ('General Surgeon', 'General Surgeon'), ('Anesthesia', 'Anesthesia'), ('Pulmonary & Sleep Med', 'Pulmonary & Sleep Med'), ('Pathology', 'Pathology'), ('Plastic & Cosmetic', 'Plastic & Cosmetic'), ('Psychiatric', 'Psychiatric'), ('Physiotherapist', 'Physiotherapist')], max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phonenumber', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=250, null=True)),
                ('speciality', models.CharField(max_length=250, null=True)),
                ('image', models.ImageField(upload_to='service/img')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('joining_date', models.DateField()),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('phonenumber', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('bloodgroup', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('phonenumber', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('bloodgroup', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('medical_typ', models.CharField(max_length=255)),
                ('buy_price', models.CharField(max_length=255)),
                ('sell_price', models.CharField(max_length=255)),
                ('c_gst', models.CharField(max_length=255)),
                ('s_gst', models.CharField(max_length=255)),
                ('batch_no', models.CharField(max_length=255)),
                ('shelf_no', models.CharField(max_length=255)),
                ('expire_date', models.DateField()),
                ('mfg_date', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('in_stock_total', models.IntegerField()),
                ('qty_in_strip', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.company')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('salt_name', models.CharField(max_length=255)),
                ('salt_qty', models.CharField(max_length=255)),
                ('salt_qty_type', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('salary_date', models.DateField()),
                ('salary_amount', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeBank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_account_no', models.CharField(max_length=255)),
                ('ifsc_no', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.employee')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyBank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_account_no', models.CharField(max_length=255)),
                ('ifsc_no', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(choices=[(1, 'Debit'), (2, 'Credit')], max_length=255)),
                ('transaction_amt', models.CharField(max_length=255)),
                ('transaction_date', models.DateField()),
                ('payment_mode', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.company')),
            ],
        ),
        migrations.CreateModel(
            name='BillDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.bill')),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.medicine')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.customer'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientname', models.CharField(max_length=50)),
                ('patientemail', models.EmailField(max_length=50)),
                ('appointmentdate', models.DateField(max_length=10)),
                ('appointmenttime', models.TimeField(max_length=10)),
                ('symptoms', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
                ('prescription', models.CharField(max_length=200)),
                ('doctorname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.doctor')),
            ],
        ),
    ]
