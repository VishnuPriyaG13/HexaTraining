use hospital_management;

INSERT INTO departments VALUES
(1, 'Cardiology'),
(2, 'Neurology'),
(3, 'Orthopedics'),
(4, 'Pediatrics'),
(5, 'General Medicine');

INSERT INTO patients VALUES
(1,  'Aarav','Male',34, 'Chennai', '9876543210'),
(2,  'Priya','Female', 28, 'Coimbatore','9876543211'),
(3,  'Ravi', 'Male',   45, 'Madurai','9876543212'),
(4,  'Sneha','Female', 32, 'Chennai','9876543213'),
(5,  'Karthik','Male',   55, 'Salem','9876543214'),
(6,  'Divya','Female', 22, 'Trichy', '9876543215'),
(7,  'Arjun','Male',   40, 'Chennai','9876543216'),
(8,  'Meena','Female', 60, 'Madurai','9876543217'),
(9,  'Suresh','Male',   38, 'Coimbatore','9876543218'),
(10, 'Lakshmi','Female', 50, 'Chennai','9876543219'),
(11, 'Vijay','Male',   29, 'Salem','9876543220'),
(12, 'Kavitha','Female', 47, 'Trichy','9876543221');

INSERT INTO doctors VALUES
(1, 'Dr. Ramesh Kumar',   'Cardiologist',      1,  800.00),
(2, 'Dr. Sunita Pillai',  'Neurologist',       2,  900.00),
(3, 'Dr. Anil Menon',     'Orthopedic Surgeon',3,  750.00),
(4, 'Dr. Preethi Nair',   'Pediatrician',      4,  600.00),
(5, 'Dr. Gopal Iyer',     'General Physician', 5,  500.00),
(6, 'Dr. Kavitha Raj',    'Cardiologist',      1,  850.00),
(7, 'Dr. Suresh Das',     'Neurologist',       2,  950.00),
(8, 'Dr. Meena Anand',    'Orthopedic Surgeon',99, 700.00);

INSERT INTO appointments VALUES
(1,  1,  1, '2024-01-05', 'Completed'),
(2,  2,  2, '2024-01-08', 'Completed'),
(3,  3,  3, '2024-01-10', 'Completed'),
(4,  4,  4, '2024-01-12', 'Completed'),
(5,  5,  5, '2024-01-15', 'Completed'),
(6,  6,  6, '2024-01-18', 'Completed'),
(7,  7,  7, '2024-01-20', 'Completed'),
(8,  8,  3, '2024-01-22', 'Completed'),
(9,  9,  1, '2024-01-25', 'Completed'),
(10, 10, 2, '2024-01-28', 'Completed'),
(11, 11, 5, '2024-02-01', 'Completed'),
(12, 12, 4, '2024-02-03', 'Completed'),
(13, 1,  6, '2024-02-05', 'Completed'),
(14, 2,  7, '2024-02-08', 'Completed'),
(15, 3,  1, '2024-02-10', 'Completed'),
(16, 4,  2, '2024-02-12', 'Cancelled'),
(17, 5,  3, '2024-02-15', 'Cancelled'),
(18, 6,  4, '2024-02-18', 'Pending'),
(19, 99, 1, '2024-02-20', 'Pending'),
(20, 1,  99,'2024-02-22', 'Pending');

INSERT INTO treatments VALUES
(1,  1,  'ECG Test',             500.00),
(2,  2,  'MRI Scan',            2500.00),
(3,  3,  'X-Ray',                800.00),
(4,  4,  'Blood Test',           300.00),
(5,  5,  'General Checkup',      200.00),
(6,  6,  'Echo Cardiogram',     1500.00),
(7,  7,  'CT Scan',             3000.00),
(8,  8,  'Knee Surgery',        8000.00),
(9,  9,  'Angioplasty',        15000.00),
(10, 10, 'Brain MRI',           4000.00),
(11, 11, 'Fever Treatment',      150.00),
(12, 12, 'Vaccination',          250.00),
(13, 13, 'Stress Test',         1200.00),
(14, 14, 'Nerve Conduction',    1800.00),
(15, 15, 'Bypass Surgery',     20000.00);

INSERT INTO bills VALUES
(1,  1,  1,  '2024-01-05', 1300.00,  'Paid'),
(2,  2,  2,  '2024-01-08', 3400.00,  'Paid'),
(3,  3,  3,  '2024-01-10', 1550.00,  'Paid'),
(4,  4,  4,  '2024-01-12', 900.00,   'Paid'),
(5,  5,  5,  '2024-01-15', 700.00,   'Paid'),
(6,  6,  6,  '2024-01-18', 2350.00,  'Paid'),
(7,  7,  7,  '2024-01-20', 3950.00,  'Paid'),
(8,  8,  8,  '2024-01-22', 8750.00,  'Paid'),
(9,  9,  9,  '2024-01-25', 15800.00, 'Paid'),
(10, 10, 10, '2024-01-28', 4900.00,  'Paid'),
(11, 11, 11, '2024-02-01', 650.00,   'Paid'),
(12, 12, 12, '2024-02-03', 850.00,   'Unpaid'),
(13, 1,  13, '2024-02-05', 2000.00,  'Unpaid'),
(14, 4,  16, '2024-02-12', 600.00,   'Unpaid'),
(15, 5,  17, '2024-02-15', 500.00,   'Unpaid');

INSERT INTO payments VALUES
(1,  1,  'Cash',         1300.00,  'Completed'),
(2,  2,  'Card',         3400.00,  'Completed'),
(3,  3,  'UPI',          1550.00,  'Completed'),
(4,  4,  'Cash',         900.00,   'Completed'),
(5,  5,  'Card',         700.00,   'Completed'),
(6,  6,  'UPI',          2350.00,  'Completed'),
(7,  7,  'Cash',         3950.00,  'Completed'),
(8,  8,  'Card',         8750.00,  'Completed'),
(9,  9,  'UPI',          15800.00, 'Completed'),
(10, 10, 'Cash',         4900.00,  'Completed'),
(11, 11, 'Card',         650.00,   'Completed'),
(12, 14, 'UPI',          400.00,   'Partial'),
(13, 15, 'Cash',         0.00,     'Pending'),
(14, 4,  'Net Banking',  900.00,   'Completed'),
(15, 5,  'UPI',          700.00,   'Completed');
