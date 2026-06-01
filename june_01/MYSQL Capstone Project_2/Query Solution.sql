use hospital_management;

select * from patients;
select * from doctors;
select * from patients
where city = 'Hyderabad';
select d.doctor_name from doctors d
join departments dp on d.department_id = dp.department_id
where dp.department_name = 'Cardiology';

select * from appointments
where appointment_date > '2026-01-01';

select * from appointments
where appointment_status = 'Cancelled';

select * from bills
where total_amount > 5000;

select * from payments
where payment_mode = 'UPI';

select * from patients
where age between 30 and 50;

select * from doctors
where consultation_fee > 800;

select count(*) as total_patients from patients;

select count(*) as total_doctors from doctors;

select count(*) as total_appointments from appointments;

select avg(consultation_fee) as avg_consultation_fee from doctors;

select max(treatment_cost) as highest_treatment_cost from treatments;

select sum(total_amount) as total_billing_amount from bills;

select sum(paid_amount) as total_paid_amount from payments;

select city, count(*) as total_patients
from patients
group by city;

select specialization, count(*) as total_doctors
from doctors
group by specialization;

select appointment_status, count(*) as total_appointments
from appointments
group by appointment_status;

select p.patient_name, a.appointment_date, a.appointment_status
from patients p
join appointments a on p.patient_id = a.patient_id;

select d.doctor_name, dp.department_name
from doctors d
join departments dp on d.department_id = dp.department_id;

select p.patient_name, d.doctor_name, a.appointment_date
from patients p
join appointments a on p.patient_id = a.patient_id
join doctors d on a.doctor_id = d.doctor_id;

select a.appointment_id, t.treatment_name, t.treatment_cost
from appointments a
join treatments t on a.appointment_id = t.appointment_id;

select b.bill_id, p.patient_name, b.total_amount
from bills b
join patients p on b.patient_id = p.patient_id;

select b.bill_id, py.payment_mode, py.paid_amount, py.payment_status
from bills b
join payments py on b.bill_id = py.bill_id;

select p.patient_name, d.doctor_name, dp.department_name,
a.appointment_date, a.appointment_status,
t.treatment_name, t.treatment_cost,
b.total_amount as bill_amount, py.payment_status
from appointments a
join patients p on a.patient_id = p.patient_id
join doctors d on a.doctor_id = d.doctor_id
join departments dp on d.department_id = dp.department_id
left join treatments t on a.appointment_id = t.appointment_id
left join bills b on a.appointment_id = b.appointment_id
left join payments py on b.bill_id = py.bill_id;

select d.doctor_name, count(a.appointment_id) as total_appointments
from doctors d
join appointments a on d.doctor_id = a.doctor_id
group by d.doctor_name;

select dp.department_name, count(a.appointment_id) as total_appointments
from departments dp
join doctors d on dp.department_id = d.department_id
join appointments a on d.doctor_id = a.doctor_id
group by dp.department_name;

select dp.department_name, sum(b.total_amount) as total_revenue
from departments dp
join doctors d on dp.department_id = d.department_id
join appointments a on d.doctor_id = a.doctor_id
join bills b on a.appointment_id = b.appointment_id
group by dp.department_name;

select treatment_name, sum(treatment_cost) as total_treatment_cost
from treatments
group by treatment_name;

select p.city, sum(b.total_amount) as total_billing
from patients p
join bills b on p.patient_id = b.patient_id
group by p.city;

select d.doctor_name, count(a.appointment_id) as total_appointments
from doctors d
join appointments a on d.doctor_id = a.doctor_id
group by d.doctor_name
having count(a.appointment_id) > 2;

select dp.department_name, sum(b.total_amount) as total_revenue
from departments dp
join doctors d on dp.department_id = d.department_id
join appointments a on d.doctor_id = a.doctor_id
join bills b on a.appointment_id = b.appointment_id
group by dp.department_name
having sum(b.total_amount) > 20000;

select city, count(*) as total_patients
from patients
group by city
having count(*) > 2;

select * from patients
where patient_id in (select distinct patient_id from appointments);

select * from patients
where patient_id not in (select distinct patient_id from appointments);

select * from doctors
where doctor_id not in (select distinct doctor_id from appointments);

select * from bills
where total_amount > (select avg(total_amount) from bills);

select * from patients
where patient_id = (select patient_id from bills
order by total_amount desc limit 1);

select * from doctors
where consultation_fee > (select avg(consultation_fee) from doctors);

select * from patients
where patient_id in (
select a.patient_id from appointments a
join doctors d on a.doctor_id = d.doctor_id
where d.department_id = (select department_id from departments
where department_name = 'Cardiology'));

select * from bills
where bill_status = 'Unpaid';

select * from appointments
where appointment_id in (select distinct appointment_id from treatments);

select * from patients
where patient_id in (
select patient_id from bills
group by patient_id
having sum(total_amount) > (
select avg(total_billing) from (
select patient_id, sum(total_amount) as total_billing
from bills
group by patient_id) as avg_table));

select * from appointments
where appointment_id not in (select distinct appointment_id from treatments);

select * from bills
where bill_id not in (select distinct bill_id from payments);

select * from payments
where paid_amount is null or paid_amount = 0;

select * from appointments
where appointment_status = 'Cancelled'
and appointment_id in (select distinct appointment_id from bills);

select b.bill_id, b.total_amount, py.paid_amount
from bills b
join payments py on b.bill_id = py.bill_id
where b.bill_status = 'Paid'
and py.paid_amount < b.total_amount;

select * from doctors
where department_id not in (select department_id from departments);

select * from appointments
where patient_id not in (select patient_id from patients)
or doctor_id not in (select doctor_id from doctors);

select p.patient_name, p.city,
count(distinct a.appointment_id) as total_appointments,
sum(b.total_amount) as total_bill_amount,
sum(py.paid_amount) as total_paid_amount,
sum(b.total_amount) - sum(py.paid_amount) as pending_amount
from patients p
left join appointments a on p.patient_id = a.patient_id
left join bills b on p.patient_id = b.patient_id
left join payments py on b.bill_id = py.bill_id
group by p.patient_name, p.city;
