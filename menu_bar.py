from PyQt5.QtWidgets import QAction,qApp

class MenuBar():

    def __init__(self,parent,tabsObj):
        bar = parent.menuBar()
        self.tabsObj = tabsObj

        # System Menu
        system = bar.addMenu("System")

        hide = QAction('Show/Hide Shortcut',parent)
        hide.setShortcut('Ctrl+F12')
        system.addAction(hide)

        lock = QAction('Lock',parent)
        lock.setShortcut('Ctrl+F7')
        system.addAction(lock)

        log_off = QAction('Log off',parent)
        log_off.setShortcut('Ctrl+F9')
        system.addAction(log_off)

        quit = QAction('Exit',parent)
        quit.setShortcut('Ctrl+F8')
        system.addAction(quit)

        # Walz_Options Menu
        walz_options = bar.addMenu("Walz Clinic Options")
        general = walz_options.addMenu('General')




        general_settings = QAction('General Settings',parent)
        # general_settings.triggered.connect(self.actionClicked)
        # general_settings.triggered.connect(lambda: self.tabsObj.addTabs(general_settings.text()))
        general_settings.triggered.connect(lambda: self.actionClicked(general_settings))
        general.addAction(general_settings)
        general_master = QAction('OP Settings Master',parent)
        general.addAction(general_master)
        general_voucher = QAction('General Voucher',parent)
        general.addAction(general_voucher)
        general_workshop = QAction('Work Shop Form',parent)
        general.addAction(general_workshop)
        general_scanning = QAction('Photo Scanning Utility',parent)
        general.addAction(general_scanning)

        # Patient Information
        patient_info = walz_options.addMenu('Patient Information')
        patient_registration = QAction('Patient Registration',parent)
        patient_info.addAction(patient_registration)
        patient_info_sheet = QAction('Patient Info Sheet',parent)
        patient_info.addAction(patient_info_sheet)
        patient_deposit = QAction('Patients Deposit Register',parent)
        patient_info.addAction(patient_deposit)

        # Walz_Options - Out Patient
        o_patient_dept = walz_options.addMenu('Out-Patient Department')

        op_register = QAction('OP Register', parent)
        o_patient_dept.addAction(op_register)

        op_discharge = QAction('Discharge Register', parent)
        o_patient_dept.addAction(op_discharge)

        op_followup = QAction('Follow-up Visit Register', parent)
        o_patient_dept.addAction(op_followup)

        op_diagnosis = QAction('Patient Diagnosis Details', parent)
        o_patient_dept.addAction(op_diagnosis)

        op_recommendation = QAction('Doctors Comments And Recommendation', parent)
        o_patient_dept.addAction(op_recommendation)

        op_prescription = QAction('Patient Prescription Details', parent)
        o_patient_dept.addAction(op_prescription)

        op_transaction = QAction('Patient Transaction', parent)
        o_patient_dept.addAction(op_transaction)

        op_utility = QAction('Patient Transaction Utility', parent)
        o_patient_dept.addAction(op_utility)

        op_record = QAction('Medical Record Management', parent)
        o_patient_dept.addAction(op_record)


        # Walz_Options - In Patient
        i_patient_dept = walz_options.addMenu('In-Patient Department')
        ip_register = QAction('Inpatient Registration',parent)
        i_patient_dept.addAction(ip_register)

        # Walz_Options - Master
        masters = walz_options.addMenu('Masters')
        master_services = QAction('Service Master',parent)
        masters.addAction(master_services)
        master_account = QAction('Account Head Register',parent)
        masters.addAction(master_account)
        master_expense = QAction('Expense Master',parent)
        masters.addAction(master_expense)
        master_diagnosis = QAction('Diagnosis Master',parent)
        masters.addAction(master_diagnosis)
        master_investigation = QAction('Investigation Master',parent)
        masters.addAction(master_investigation)
        master_doctor = QAction('Doctor Specialization Master',parent)
        masters.addAction(master_doctor)
        master_resources = QAction('Resource Master',parent)
        masters.addAction(master_resources)

        # Accounts
        accounts = walz_options.addMenu('Accounts')
        patient_billing = QAction('Patient Billing',parent)
        accounts.addAction(patient_billing)

        # Reports
        reports = walz_options.addMenu('Reports')
        report = QAction('Reports',parent)
        report.setShortcut('Ctrl+F6')
        reports.addAction(report)

        report_accounts = QAction('Accounts Reports',parent)
        reports.addAction(report_accounts)

        # Administration
        admin = walz_options.addMenu('Administration')
        settings_company = QAction('Company Profile Settings',parent)
        admin.addAction(settings_company)
        settings_branch = QAction('Branch Profile Settings',parent)
        admin.addAction(settings_branch)
        settings_users = QAction('User Right Assignment',parent)
        admin.addAction(settings_users)
        settings_prescription = QAction('Prescription Template Master',parent)
        admin.addAction(settings_prescription)
        settings_expense = QAction('Expense Charge Settings',parent)
        admin.addAction(settings_expense)

        # Appointments
        appointments = walz_options.addMenu('Appointments')
        appointment = QAction('Appointments',parent)
        appointment.setShortcut('Ctrl+F3')
        appointments.addAction(appointment)

        appointment_register = QAction('Appointment Visit Register',parent)
        appointments.addAction(appointment_register)

        # Employee Information
        emp_info = walz_options.addMenu('Employee Information')

        emp_reg = QAction('Employee Registration',parent)
        emp_info.addAction(emp_reg)

        emp_account = QAction('Employee Account Master',parent)
        emp_info.addAction(emp_account)

        emp_bank_master = QAction('Bank Master',parent)
        emp_info.addAction(emp_bank_master)

        emp_bank_account = QAction('Bank Account Register',parent)
        emp_info.addAction(emp_bank_account)

        emp_bank_account_transaction = QAction('Bank Account Transaction',parent)
        emp_info.addAction(emp_bank_account_transaction)

        emp_designation = QAction('Employee Designation Master',parent)
        emp_info.addAction(emp_designation)

        emp_staff_master = QAction('Employee Staff Master',parent)
        emp_info.addAction(emp_staff_master)

        emp_shift = QAction('Employee Shift Master',parent)
        emp_info.addAction(emp_shift)

        emp_account_transaction = QAction('Employee Account Transaction',parent)
        emp_info.addAction(emp_account_transaction)

        emp_user_maintenance = QAction('User Maintenance',parent)
        emp_info.addAction(emp_user_maintenance)

        emp_attendance_reg = QAction('Employee Attendance Register',parent)
        emp_info.addAction(emp_attendance_reg)

        # Doctor Details
        doctor_details = walz_options.addMenu('Doctor Details')
        doctor_master = QAction('Doctor Master',parent)
        doctor_details.addAction(doctor_master)
        doctor_duty = QAction('Doctor Duty Timings Register',parent)
        doctor_details.addAction(doctor_duty)
        doctor_leave = QAction('Doctor Leave Register',parent)
        doctor_details.addAction(doctor_leave)
        doctor_refer = QAction('Refer In Doctor Master',parent)
        doctor_details.addAction(doctor_refer)

        # Insurance Section
        insurance_sec = walz_options.addMenu('Insurance Section')
        insurance_claim = QAction('Insurance Claim',parent)
        insurance_sec.addAction(insurance_claim)
        insurance_master = QAction('Insurance Master',parent)
        insurance_sec.addAction(insurance_master)

        # Utility
        utility = bar.addMenu("Utility")
        pword_mangement = QAction('Password Management',parent)
        utility.addAction(pword_mangement)

        about = bar.addMenu("About/Help")
        about_about = QAction('About',parent)
        about.addAction(about_about)
        about_help = QAction('Help',parent)
        about.addAction(about_help)
        about_update = QAction('Update',parent)
        about.addAction(about_update)

        # Exit

        exit = QAction("Exit",parent)
        exit.setStatusTip('Exit application')
        exit.triggered.connect(qApp.quit)
        bar.addAction(exit)

    def actionClicked(self,checked):
        self.tabsObj.addTabs(checked.text())