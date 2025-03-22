from imports import *

app = Flask(__name__, static_folder='static')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.template_filter('time_ago')
def time_ago_filter(timestamp):
    now = datetime.now()
    delta = now - timestamp
    if delta.days > 0:
        return f"{delta.days} days ago"
    elif delta.seconds > 3600:
        return f"{delta.seconds // 3600} hours ago"
    elif delta.seconds > 60:
        return f"{delta.seconds // 60} minutes ago"
    else:
        return "Just now"
###############################################################################

# Database connector
app.config['SECRET_KEY'] = 'Fl0r3nz!OsMh@r#Val3r1e$X9Y7T'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'filsha'

def get_db_connection():
    return mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

#for total gb file uploaded by user 
def calculate_total_uploaded_size(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT filename FROM files WHERE owner_id = %s", (user_id,))
    files = cursor.fetchall()
    cursor.close()
    conn.close()

    total_size = 0
    for file in files:
        file_path = os.path.join('uploads', file[0])
        if os.path.exists(file_path):
            total_size += os.path.getsize(file_path)
    return total_size / (1024 * 1024 * 1024)  # Convert bytes to GB

def get_expiration_time(expiration_duration):
    if expiration_duration == '1h':
        return datetime.now() + timedelta(hours=1)
    elif expiration_duration == '1d':
        return datetime.now() + timedelta(days=1)
    elif expiration_duration == '1w':
        return datetime.now() + timedelta(weeks=1)
    else:
        return None
############################# FOR total virus detected ######################################
#for user
def calculate_total_viruses_detected(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM files WHERE owner_id = %s AND virus_detected = TRUE", (user_id,))
    total_viruses = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total_viruses
#for admin
def calculate_total_viruses_detected_all_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM files WHERE virus_detected = TRUE")
    total_viruses = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total_viruses
############################## file quota and limit size upload ###############################
def calculate_file_size_breakdown(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT size FROM files WHERE owner_id = %s", (user_id,))
    files = cursor.fetchall()
    cursor.close()
    conn.close()

    # Initialize sizes in GB
    small_gb = 0.0  # Files < 100MB
    medium_gb = 0.0  # 100MB ≤ Files < 1GB
    large_gb = 0.0   # Files ≥ 1GB

    for file in files:
        size_bytes = file[0]
        size_gb = size_bytes / (1024 ** 3)  # Convert bytes to GB

        if size_gb < 0.1:  # 100MB = 0.1GB
            small_gb += size_gb
        elif 0.1 <= size_gb < 1:
            medium_gb += size_gb
        else:
            large_gb += size_gb

    return {
        'small_gb': round(small_gb, 2),
        'medium_gb': round(medium_gb, 2),
        'large_gb': round(large_gb, 2)
    }

############################## ADMIN FUNCTIONALITY ###########################################
#total of file size
def generate_username(first_name, last_name):
    # Replace spaces in the first name with underscores
    first_name_cleaned = first_name.replace(" ", "_").lower()
    last_name_cleaned = last_name.lower()
    
    # Generate the base username
    base_username = f"{first_name_cleaned}.{last_name_cleaned}"
    username = base_username
    counter = 1

    conn = get_db_connection()
    cursor = conn.cursor()
    while True:
        cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        if not cursor.fetchone():
            break
        username = f"{base_username}{counter}"
        counter += 1
    cursor.close()
    conn.close()

    return username

def generate_password():
    # Generate a random password with 8 characters
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(8))

def calculate_total_uploaded_size_all_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT owner_id, filename FROM files")
    files = cursor.fetchall()
    cursor.close()
    conn.close()

    total_size = 0
    for file in files:
        file_path = os.path.join('uploads', file[1])
        if os.path.exists(file_path):
            total_size += os.path.getsize(file_path)
    return total_size / (1024 * 1024 * 1024)  # Convert bytes to GB


# total of users
def get_user_statistics():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch total number of users
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    # Fetch total number of barangay captains
    cursor.execute("SELECT COUNT(*) FROM brgycaptain")
    total_brgycaptain = cursor.fetchone()[0]

    # Fetch total number of government positions
    cursor.execute("SELECT COUNT(*) FROM government_position")
    total_government_position = cursor.fetchone()[0]

    # Fetch total number of municipal employees
    cursor.execute("SELECT COUNT(*) FROM employee")
    total_employee = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return {
        'total_users': total_users,
        'total_brgycaptain': total_brgycaptain,
        'total_government_position': total_government_position,
        'total_employee': total_employee
    }
    
#activity log
def log_activity(user_id, action, description=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO activity_log (user_id, action, description)
        VALUES (%s, %s, %s)
    """, (user_id, action, description))
    conn.commit()
    cursor.close()
    conn.close()

def get_users_with_details():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT 
                u.id, 
                u.username, 
                u.role, 
                CONCAT(
                    COALESCE(b.first_name, g.first_name, e.first_name, ''), ' ',
                    COALESCE(b.middle_name, g.middle_name, e.middle_name, ''), ' ',
                    COALESCE(b.last_name, g.last_name, e.last_name, '')
                ) AS full_name,
                COALESCE(b.email, g.email, e.email) AS email,
                COALESCE(b.contact_number, g.contact_number, e.contact_number) AS contact_number,
                COALESCE(b.gender, g.gender, e.gender) AS gender,
                COALESCE(b.age, g.age, e.age) AS age,
                COALESCE(b.position, g.government_position, e.position) AS position,
                COALESCE(SUM(f.size) / (1024 * 1024 * 1024), 0) AS total_uploaded_size
            FROM users u
            LEFT JOIN brgycaptain b ON u.id = b.user_id
            LEFT JOIN government_position g ON u.id = g.user_id
            LEFT JOIN employee e ON u.id = e.user_id
            LEFT JOIN files f ON u.id = f.owner_id
            GROUP BY u.id
        """)
        users = cursor.fetchall()
        return users
    except Exception as e:
        print(f"Error fetching user details: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

###############################################################################
# Function to send SMS
def send_sms(phone_number, message):
    username = "" 
    password = "" 
    url = "https://api.sms-gate.app/3rdparty/v1/message"
    
    # Use the correct payload structure
    payload = {
        "message": message,
        "phoneNumbers": [phone_number]
    }
    
    # Set the correct headers
    headers = {"Content-Type": "application/json"}
    
    try:
        # Send the request with JSON payload and authentication
        response = requests.post(url, json=payload, headers=headers, auth=(username, password))
        
        # Log the response for debugging
        print(f"SMS API Response: {response.status_code}, {response.text}")
        
        # Check for successful response
        if response.status_code in [200, 201, 202]:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error sending SMS: {e}")
        return False


def generate_otp():
    return ''.join(random.choice('0123456789') for _ in range(6))

def send_otp_via_sms(phone_number, otp):
    message = f"Your OTP for login is: {otp}"
    return send_sms(phone_number, message)
###############################################################################
def delete_expired_files():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='filsha'
    )
    cursor = conn.cursor()

    # Fetch expired files
    cursor.execute("SELECT id, filename FROM files WHERE expiration_time IS NOT NULL AND expiration_time <= NOW()")
    expired_files = cursor.fetchall()

    for file_id, filename in expired_files:
        # Delete the file from the filesystem
        file_path = os.path.join('uploads', filename)
        if os.path.exists(file_path):
            os.remove(file_path)

        # Delete the file record from the database
        cursor.execute("DELETE FROM files WHERE id = %s", (file_id,))
        conn.commit()

    cursor.close()
    conn.close()

# Run this function periodically (e.g., using a cron job or a scheduler)
delete_expired_files()

###############################################################################

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Admin Credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'

# Generate and save an encryption key (run this once)
if not os.path.exists('key.key'):
    with open('key.key', 'wb') as key_file:
        key_file.write(Fernet.generate_key())

with open('key.key', 'rb') as key_file:
    encryption_key = key_file.read()

cipher = Fernet(encryption_key)

#THIS IS FOR AES ENCRYPTION
def generate_aes_key():
    return os.urandom(32)  # 256-bit key

# Encrypt data with AES
def encrypt_aes(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return cipher.iv + ct_bytes

# Decrypt data with AES
def decrypt_aes(encrypted_data, key):
    iv = encrypted_data[:AES.block_size]
    ct = encrypted_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt


# Function to load suspicious hashes from a file
def load_suspicious_hashes(file_path):
    with open(file_path, 'r') as file:
        return set(line.strip() for line in file)

# Load suspicious hashes from the file
SUSPICIOUS_HASHES = load_suspicious_hashes('MD5 Hahses.txt')

# Disable caching to force auto-logout
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

# User Loader
@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, password, password_changed, profile_picture FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        return User(user[0], user[1], user[2], user[3], user[4])
    return None

# User class
class User(UserMixin):
    def __init__(self, id, username, password, password_changed=False, profile_picture=None):
        self.id = id
        self.username = username
        self.password = password
        self.password_changed = password_changed
        self.profile_picture = profile_picture
    
 
# Add Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = ''  
app.config['MAIL_PASSWORD'] = ''  
app.config['MAIL_DEFAULT_SENDER'] = '' 

mail = Mail(app)



        
@app.route('/')
def index():
    # Render the landing page
    #return render_template('landing_page.html')
    return redirect(url_for('login'))

########################################### - ADMIN ROUTES - ###################################################
# Routes
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin'] = True
            session['admin_username'] = username  # Store admin username in session
            log_activity(None, 'admin_login', f'Admin {username} logged in.')
            flash('Admin logged in successfully.', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid admin credentials.', 'danger')
    return render_template('admin/admin_login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin' not in session:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('admin_login'))

    total_uploaded_gb = calculate_total_uploaded_size_all_users()
    user_statistics = get_user_statistics()
    total_viruses_detected = calculate_total_viruses_detected_all_users()

    return render_template('admin/admin_dashboard.html', 
                           admin_username=session.get('admin_username'), 
                           total_uploaded_gb=total_uploaded_gb,
                           total_users=user_statistics['total_users'],
                           total_brgycaptain=user_statistics['total_brgycaptain'],
                           total_government_position=user_statistics['total_government_position'],
                           total_employee=user_statistics['total_employee'],
                           total_viruses_detected=total_viruses_detected)
@app.route('/admin/user_list')
def admin_user_list():
    if 'admin' not in session:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('admin_login'))

    try:
        users = get_users_with_details()
        return render_template('admin/admin_user_list.html',
                               admin_username=session.get('admin_username'),
                               users=users)
    except Exception as e:
        flash(f"An error occurred: {e}", "danger")
        return redirect(url_for('admin_dashboard'))

# Routes
@app.route('/admin/add_user', methods=['GET', 'POST'])
def admin_add_user():
    if 'admin' not in session:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('admin_login'))

    if request.method == 'POST':
        # Fetch form data
        first_name = request.form['firstName']
        middle_name = request.form.get('middleName', '')
        last_name = request.form['lastName']
        gender = request.form['gender']
        age = request.form['age']
        contact_number = request.form['contactNumber']
        role = request.form['role']
        government_position = request.form.get('governmentPosition', '')
        barangay = request.form.get('barangay', '')
        department = request.form.get('department', '')
        position = request.form.get('employeePosition', '')  # Updated to use employeePosition
        email = request.form['email']

        # Generate username and password
        username = generate_username(first_name, last_name)
        password = generate_password()

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Insert into users table
            cursor.execute("""
                INSERT INTO users (username, password, role, password_changed)
                VALUES (%s, %s, %s, %s)
            """, (username, hashed_password, role, False))  # Set password_changed to False
            user_id = cursor.lastrowid

            # Insert into role-specific table
            if role == 'barangay-captain':
                cursor.execute("""
                    INSERT INTO brgycaptain 
                    (user_id, first_name, middle_name, last_name, gender, age, contact_number, position, email, barangay)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (user_id, first_name, middle_name, last_name, gender, age, contact_number, "Barangay Captain", email, barangay))

            elif role == 'government-position':
                cursor.execute("""
                    INSERT INTO government_position 
                    (user_id, first_name, middle_name, last_name, gender, age, contact_number, government_position, email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (user_id, first_name, middle_name, last_name, gender, age, contact_number, government_position, email))

            elif role == 'municipal-employee':
                cursor.execute("""
                    INSERT INTO employee 
                    (user_id, first_name, middle_name, last_name, gender, age, contact_number, department, position, email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (user_id, first_name, middle_name, last_name, gender, age, contact_number, department, position, email))

            conn.commit()

            # Prepare the message for email and SMS
            message = f"""
            Your account has been created successfully.
            Username: {username}
            Password: {password}
            
            You will be required to change your password on your first login.
            """

            # Send email with username and password
            msg = Message('Your Account Information', recipients=[email])
            msg.body = message
            mail.send(msg)

            # Send SMS with the same account information
            sms_status = send_sms(contact_number, message)

            if sms_status == 200:
                flash('User added successfully, email and SMS sent.', 'success')
            else:
                flash('User added successfully, email sent but SMS failed.', 'warning')

        except Exception as e:
            flash(f"Error: {e}", "danger")
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('admin_dashboard'))

    return render_template('admin/admin_add_user.html', admin_username=session.get('admin_username'))

@app.route('/admin/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if 'admin' not in session:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('admin_login'))

    if request.method == 'POST':
        # Fetch form data
        first_name = request.form['firstName']
        middle_name = request.form.get('middleName', '')
        last_name = request.form['lastName']
        gender = request.form['gender']
        age = request.form['age']
        contact_number = request.form['contactNumber']
        email = request.form['email']
        username = request.form['username']
        password = request.form.get('password')  # New password field

        # Fetch the user's current role
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT role FROM users WHERE id = %s", (user_id,))
        role = cursor.fetchone()[0]

        try:
            # Update users table
            if password:
                # Hash the new password
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                cursor.execute("""
                    UPDATE users 
                    SET username = %s, password = %s
                    WHERE id = %s
                """, (username, hashed_password, user_id))
            else:
                # Update username only if password is not provided
                cursor.execute("""
                    UPDATE users 
                    SET username = %s
                    WHERE id = %s
                """, (username, user_id))

            # Update role-specific table
            if role == 'barangay-captain':
                barangay = request.form.get('barangay', '')
                position = "Barangay Captain"  # Default position for barangay captain
                cursor.execute("""
                    UPDATE brgycaptain 
                    SET first_name = %s, middle_name = %s, last_name = %s, gender = %s, age = %s, 
                        contact_number = %s, position = %s, email = %s, barangay = %s
                    WHERE user_id = %s
                """, (first_name, middle_name, last_name, gender, age, contact_number, position, email, barangay, user_id))

            elif role == 'government-position':
                government_position = request.form.get('governmentPosition', '')
                cursor.execute("""
                    UPDATE government_position 
                    SET first_name = %s, middle_name = %s, last_name = %s, gender = %s, age = %s, 
                        contact_number = %s, government_position = %s, email = %s
                    WHERE user_id = %s
                """, (first_name, middle_name, last_name, gender, age, contact_number, government_position, email, user_id))

            elif role == 'municipal-employee':
                department = request.form.get('department', '')
                position = request.form.get('position', '')
                cursor.execute("""
                    UPDATE employee 
                    SET first_name = %s, middle_name = %s, last_name = %s, gender = %s, age = %s, 
                        contact_number = %s, department = %s, position = %s, email = %s
                    WHERE user_id = %s
                """, (first_name, middle_name, last_name, gender, age, contact_number, department, position, email, user_id))

            conn.commit()
            flash('User updated successfully.', 'success')
        except Exception as e:
            flash(f"Error: {e}", "danger")
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('admin_user_list'))

    # Fetch user details for pre-filling the form
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()

    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('admin_user_list'))

    # Fetch role-specific details
    role = user[3]  # role is at index 3 in the users table
    role_details = None

    if role == 'barangay-captain':
        cursor.execute("SELECT * FROM brgycaptain WHERE user_id = %s", (user_id,))
        role_details = cursor.fetchone()
    elif role == 'government-position':
        cursor.execute("SELECT * FROM government_position WHERE user_id = %s", (user_id,))
        role_details = cursor.fetchone()
    elif role == 'municipal-employee':
        cursor.execute("SELECT * FROM employee WHERE user_id = %s", (user_id,))
        role_details = cursor.fetchone()

    cursor.close()
    conn.close()

    if not role_details:
        flash('Role-specific details not found.', 'danger')
        return redirect(url_for('admin_user_list'))

    # Combine user and role-specific details into a dictionary
    user_details = {
        'id': user[0],
        'username': user[1],
        'role': user[3],
        'first_name': role_details[2] if len(role_details) > 2 else '',
        'middle_name': role_details[3] if len(role_details) > 3 else '',
        'last_name': role_details[4] if len(role_details) > 4 else '',
        'gender': role_details[5] if len(role_details) > 5 else '',
        'age': role_details[6] if len(role_details) > 6 else '',
        'contact_number': role_details[7] if len(role_details) > 7 else '',
        'position': role_details[8] if len(role_details) > 8 else '',
        'email': role_details[9] if len(role_details) > 9 else '',
        'government_position': role_details[10] if len(role_details) > 10 and role == 'government-position' else '',
        'barangay': role_details[10] if len(role_details) > 10 and role == 'barangay-captain' else '',
        'department': role_details[10] if len(role_details) > 10 and role == 'municipal-employee' else ''
    }

    return render_template('admin/admin_edit_user.html', user=user_details)

@app.route('/admin/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if 'admin' not in session:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('admin_login'))

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Fetch the user's role to determine which role-specific table to delete from
        cursor.execute("SELECT role FROM users WHERE id = %s", (user_id,))
        role = cursor.fetchone()[0]

        # Delete from role-specific tables based on the user's role
        if role == 'barangay-captain':
            cursor.execute("DELETE FROM brgycaptain WHERE user_id = %s", (user_id,))
        elif role == 'government-position':
            cursor.execute("DELETE FROM government_position WHERE user_id = %s", (user_id,))
        elif role == 'municipal-employee':
            cursor.execute("DELETE FROM employee WHERE user_id = %s", (user_id,))

        # Delete the user from the users table
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        
        conn.commit()
        flash('User and related data deleted successfully.', 'success')
    except Exception as e:
        conn.rollback()
        flash(f"Error: {e}", "danger")
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('admin_user_list'))


# THIS IS FOR ADMIN ACTIVITY LOGS FOR USERS
@app.route('/admin/activity_log')
def admin_activity_log():
    if 'admin' not in session:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('admin_login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # Use dictionary cursor
    cursor.execute("""
        SELECT 
            activity_log.id,
            activity_log.user_id,
            activity_log.action,
            activity_log.description,
            activity_log.timestamp,
            users.username,
            files.filename,
            files.size
        FROM activity_log 
        LEFT JOIN users ON activity_log.user_id = users.id
        LEFT JOIN files ON activity_log.description LIKE CONCAT('%', files.filename, '%')
        ORDER BY activity_log.timestamp DESC
    """)
    logs = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('admin/admin_activity_log.html', admin_username=session.get('admin_username'), logs=logs)


#admin inquiries
@app.route('/admin/inquiries')
def admin_inquiries():
    if 'admin' not in session:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('admin_login'))

    # Fetch all inquiries with user details
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT 
            user_inquiries.id, 
            user_inquiries.subject, 
            user_inquiries.description, 
            user_inquiries.status, 
            user_inquiries.created_at, 
            users.username 
        FROM user_inquiries 
        LEFT JOIN users ON user_inquiries.user_id = users.id 
        ORDER BY user_inquiries.created_at DESC
    """)
    inquiries = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('admin/admin_inquiries.html', inquiries=inquiries , admin_username=session.get('admin_username'))

@app.route('/admin/resolve_inquiry/<int:inquiry_id>', methods=['POST'])
def resolve_inquiry(inquiry_id):
    if 'admin' not in session:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('admin_login'))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE user_inquiries 
        SET status = 'Resolved' 
        WHERE id = %s
    """, (inquiry_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Inquiry resolved successfully.', 'success')
    return redirect(url_for('admin_inquiries'))

@app.route('/admin/delete_inquiry/<int:inquiry_id>', methods=['POST'])
def delete_inquiry(inquiry_id):
    if 'admin' not in session:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('admin_login'))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_inquiries WHERE id = %s", (inquiry_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Inquiry deleted successfully.', 'success')
    return redirect(url_for('admin_inquiries'))

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin', None)
    session.pop('admin_username', None)  # Clear admin username from session
    flash('Admin logged out.', 'info')
    return redirect(url_for('admin_login'))

########################################## - USER ROUTES - #############################################################

# LOGIN USER FUNCTION
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        # Fetch user details from the users table
        cursor.execute("SELECT id, username, password, password_changed, role FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and bcrypt.check_password_hash(user[2], password):
            # Fetch contact_number from the role-specific table
            role = user[4]  # role is at index 4 in the users table
            contact_number = None

            if role == 'barangay-captain':
                cursor.execute("SELECT contact_number FROM brgycaptain WHERE user_id = %s", (user[0],))
                result = cursor.fetchone()
                if result:
                    contact_number = result[0]
            elif role == 'government-position':
                cursor.execute("SELECT contact_number FROM government_position WHERE user_id = %s", (user[0],))
                result = cursor.fetchone()
                if result:
                    contact_number = result[0]
            elif role == 'municipal-employee':
                cursor.execute("SELECT contact_number FROM employee WHERE user_id = %s", (user[0],))
                result = cursor.fetchone()
                if result:
                    contact_number = result[0]

            cursor.close()
            conn.close()

            if not contact_number:
                flash('Contact number not found for the user.', 'danger')
                return redirect(url_for('login'))

            login_user(User(user[0], user[1], user[2], user[3]))

            # Check if the user needs to change their password
            if not user[3]:  # password_changed is False
                # Generate and send OTP immediately after first-time login
                otp = generate_otp()
                session['otp'] = otp
                session['user_id'] = user[0]
                print(f"Generated OTP: {otp}")  # Debug: Log the generated OTP
                print(f"Sending OTP to: {contact_number}")  # Debug: Log the contact number
                if send_otp_via_sms(contact_number, otp):  # Send OTP to the user's contact number
                    flash('An OTP has been sent to your registered phone number.', 'info')
                else:
                    flash('Failed to send OTP. Please try again.', 'danger')
                flash('You must change your password before proceeding.', 'info')
                return redirect(url_for('change_password'))  # Redirect to change_password

            # Generate and send OTP for regular login
            otp = generate_otp()
            session['otp'] = otp
            session['user_id'] = user[0]
            print(f"Generated OTP: {otp}")  # Debug: Log the generated OTP
            print(f"Sending OTP to: {contact_number}")  # Debug: Log the contact number
            if send_otp_via_sms(contact_number, otp):  # Send OTP to the user's contact number
                flash('An OTP has been sent to your registered phone number.', 'info')
            else:
                flash('Failed to send OTP. Please try again.', 'danger')
            return redirect(url_for('verify_otp'))  # Redirect to OTP verification page

        else:
            flash('Invalid credentials.', 'danger')

    return render_template('login.html')


# THIS IS FOR USER DASHBOARD
STORAGE_QUOTA = 30  # in GB
@app.route('/userdashboard')
@login_required
def userdashboard():
    # Fetch user details
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (current_user.id,))
    user = cursor.fetchone()

    # Fetch the latest message per sender for the current user
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT m.id, m.message, m.created_at, m.sender_id, u.username AS sender_username
        FROM messages m
        JOIN users u ON m.sender_id = u.id
        JOIN (
            SELECT sender_id, MAX(created_at) AS latest_timestamp
            FROM messages
            WHERE receiver_id = %s
            GROUP BY sender_id
        ) latest ON m.sender_id = latest.sender_id AND m.created_at = latest.latest_timestamp
        WHERE m.receiver_id = %s
        ORDER BY m.created_at DESC
        LIMIT 2
    """, (current_user.id, current_user.id))
    latest_messages = cursor.fetchall()

    # Decrypt the messages
    for message in latest_messages:
        try:
            # Decrypt the message
            decrypted_message = cipher.decrypt(message['message'].encode('utf-8')).decode('utf-8')
            message['message'] = decrypted_message
        except Exception as e:
            print(f"Error decrypting message: {e}")
            message['message'] = "[Unable to decrypt message]"

    # Count unread messages (or total messages if no is_read column exists)
    cursor.execute("""
        SELECT COUNT(*) AS unread_count 
        FROM messages 
        WHERE receiver_id = %s
    """, (current_user.id,))
    unread_message_count = cursor.fetchone()['unread_count']

    # Calculate total uploaded size in GB
    total_uploaded_gb = calculate_total_uploaded_size(current_user.id)

    # Calculate storage usage percentage
    storage_usage_percentage = (total_uploaded_gb / STORAGE_QUOTA) * 1000  # testing

    # Calculate file size breakdown
    file_size_breakdown = calculate_file_size_breakdown(current_user.id)

    # Fetch user's role-specific details
    role = user[4]  # role is at index 4 in the users table
    role_details = None

    if role == 'barangay-captain':
        cursor.execute("SELECT * FROM brgycaptain WHERE user_id = %s", (current_user.id,))
        role_details = cursor.fetchone()
    elif role == 'government-position':
        cursor.execute("SELECT * FROM government_position WHERE user_id = %s", (current_user.id,))
        role_details = cursor.fetchone()
    elif role == 'municipal-employee':
        cursor.execute("SELECT * FROM employee WHERE user_id = %s", (current_user.id,))
        role_details = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template(
        'userdashboard.html',
        user=user,
        role_details=role_details,
        total_uploaded_gb=total_uploaded_gb,
        storage_quota=STORAGE_QUOTA,
        storage_usage_percentage=storage_usage_percentage,
        latest_messages=latest_messages,
        unread_message_count=unread_message_count,
        file_size_breakdown=file_size_breakdown,
        total_viruses_detected=calculate_total_viruses_detected(current_user.id)
    )
# THIS IS FOR THE FILESHARE 
@app.route('/fileshare', methods=['GET', 'POST'])
@login_required
def fileshare():
    if 'otp_verified' not in session:
        flash('Please verify your OTP to access the fileshare.', 'info')
        return redirect(url_for('verify_otp'))

    if request.method == 'POST':
        files = request.files.getlist('file')
        shared_with = request.form['shared_with']
        expiration_duration = request.form.get('expiration_duration')
        user_queries = request.form.get('user_queries', '')
        delete_after_download = 'delete_after_download' in request.form

        if not files or all(f.filename == '' for f in files):
            flash('No files selected.', 'danger')
            return redirect(url_for('fileshare'))

        # Validate shared_with usernames
        shared_usernames = [username.strip() for username in shared_with.split(',') if username.strip()]
        valid_usernames = []
        conn = get_db_connection()
        cursor = conn.cursor()
        
        for username in shared_usernames:
            cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
            if cursor.fetchone():
                valid_usernames.append(username)
            else:
                flash(f"Username '{username}' does not exist and will be ignored.", 'warning')

        if not valid_usernames:
            flash('No valid usernames provided for sharing.', 'danger')
            return redirect(url_for('fileshare'))

        try:
            # Process files based on count
            if len(files) > 1:
                # Process multiple files as ZIP
                virus_found = False
                zip_buffer = BytesIO()
                
                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for file in files:
                        if file.filename == '':
                            continue
                            
                        # Check file size
                        file.seek(0, os.SEEK_END)
                        file_size = file.tell()
                        file.seek(0)
                        if file_size > 1024 * 1024 * 1024:
                            flash(f'File {file.filename} exceeds 1GB limit.', 'danger')
                            continue
                            
                        # Read and check file content
                        file_data = file.read()
                        file_hash = hashlib.md5(file_data).hexdigest()
                        
                        if file_hash in SUSPICIOUS_HASHES:
                            flash(f'Virus detected in {file.filename}. Upload aborted.', 'danger')
                            virus_found = True
                            break
                            
                        zipf.writestr(file.filename, file_data)
                        
                if virus_found:
                    return redirect(url_for('fileshare'))
                    
                # Create ZIP filename with timestamp
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                zip_filename = f"files_{timestamp}.zip"
                zip_data = zip_buffer.getvalue()
                
                # Encrypt with Fernet
                encrypted_zip = cipher.encrypt(zip_data)
                
                # Encrypt with AES
                aes_key = generate_aes_key()
                double_encrypted_zip = encrypt_aes(encrypted_zip, aes_key)
                
                # Save the double-encrypted ZIP
                zip_path = os.path.join('uploads', zip_filename)
                with open(zip_path, 'wb') as f:
                    f.write(double_encrypted_zip)
                    
                # Store ZIP file details
                cursor.execute(
                    """INSERT INTO files 
                    (filename, owner_id, shared_with, created_at, expiration_time, 
                     size, user_queries, virus_detected, delete_after_download, aes_key)
                    VALUES (%s, %s, %s, NOW(), %s, %s, %s, %s, %s, %s)""",
                    (zip_filename, current_user.id, ','.join(valid_usernames),
                    get_expiration_time(expiration_duration), len(zip_data),
                    user_queries, False, delete_after_download, aes_key)
                )
                
                flash(f'{len(files)} files zipped and uploaded successfully.', 'success')
                
            else:
                # Process single file
                file = files[0]
                if file.filename == '':
                    flash('No file selected.', 'danger')
                    return redirect(url_for('fileshare'))
                
                # Check file size
                file.seek(0, os.SEEK_END)
                file_size = file.tell()
                file.seek(0)
                if file_size > 1024 * 1024 * 1024:
                    flash('File size exceeds 1GB limit.', 'danger')
                    return redirect(url_for('fileshare'))
                    
                # Read and check file content
                file_data = file.read()
                file_hash = hashlib.md5(file_data).hexdigest()
                
                if file_hash in SUSPICIOUS_HASHES:
                    flash('File contains virus. Upload aborted.', 'danger')
                    return redirect(url_for('fileshare'))
                    
                # Encrypt with Fernet
                encrypted_data = cipher.encrypt(file_data)
                
                # Encrypt with AES
                aes_key = generate_aes_key()
                double_encrypted_data = encrypt_aes(encrypted_data, aes_key)
                
                # Save the double-encrypted file
                file_path = os.path.join('uploads', file.filename)
                with open(file_path, 'wb') as f:
                    f.write(double_encrypted_data)
                    
                # Store file details
                cursor.execute(
                    """INSERT INTO files 
                    (filename, owner_id, shared_with, created_at, expiration_time, 
                     size, user_queries, virus_detected, delete_after_download, aes_key)
                    VALUES (%s, %s, %s, NOW(), %s, %s, %s, %s, %s, %s)""",
                    (file.filename, current_user.id, ','.join(valid_usernames),
                    get_expiration_time(expiration_duration), len(file_data),
                    user_queries, False, delete_after_download, aes_key)
                )
                
                flash('File uploaded successfully.', 'success')
                
            conn.commit()
            
        except Exception as e:
            conn.rollback()
            flash(f'Error during file processing: {str(e)}', 'danger')
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('fileshare'))

    # Fetch user's own files with owner's username and shared files
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Fetch user's own files along with the owner's username
    cursor.execute("""
        SELECT files.*, users.username as owner_username 
        FROM files 
        JOIN users ON files.owner_id = users.id 
        WHERE files.owner_id = %s
    """, (current_user.id,))
    user_files = cursor.fetchall()

    # Fetch files shared with the current user, including owner's username
    cursor.execute("""
        SELECT files.*, users.username as owner_username 
        FROM files 
        JOIN users ON files.owner_id = users.id 
        WHERE FIND_IN_SET(%s, files.shared_with)
    """, (current_user.username,))
    shared_files = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        'fileshare.html',
        total_uploaded_gb=calculate_total_uploaded_size(current_user.id),
        user_files=user_files,
        shared_files=shared_files,
    )

#THIS IS FOR USER PROFILE    
@app.route('/userprofile')
@login_required
def userprofile():
    if 'otp_verified' not in session:
        flash('Please verify your OTP to access the profile page.', 'info')
        return redirect(url_for('verify_otp'))

    # Fetch user details
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # Use dictionary cursor to access columns by name
    cursor.execute("SELECT * FROM users WHERE id = %s", (current_user.id,))
    user = cursor.fetchone()

    # Fetch user's role-specific details
    role = user['role']  # role is at index 4 in the users table
    role_details = None

    if role == 'barangay-captain':
        cursor.execute("SELECT * FROM brgycaptain WHERE user_id = %s", (current_user.id,))
        role_details = cursor.fetchone()
    elif role == 'government-position':
        cursor.execute("SELECT * FROM government_position WHERE user_id = %s", (current_user.id,))
        role_details = cursor.fetchone()
    elif role == 'municipal-employee':
        cursor.execute("SELECT * FROM employee WHERE user_id = %s", (current_user.id,))
        role_details = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template('userprofile.html', user=user, role_details=role_details, role=role)

# THIS IS FOR USER HISTORY
@app.route('/userhistory')
@login_required
def userhistory():
    if 'otp_verified' not in session:
        flash('Please verify your OTP to access the history page.', 'info')
        return redirect(url_for('verify_otp'))

    # Fetch uploaded files by the user
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, filename, shared_with, created_at, size, user_queries 
        FROM files 
        WHERE owner_id = %s
    """, (current_user.id,))
    uploaded_files = cursor.fetchall()

    # Fetch files sent by the user (shared with others)
    cursor.execute("""
        SELECT id, filename, shared_with, created_at, size, user_queries 
        FROM files 
        WHERE owner_id = %s AND shared_with IS NOT NULL
    """, (current_user.id,))
    sent_files = cursor.fetchall()

    # Fetch user inquiries
    cursor.execute("""
        SELECT id, subject, description, status, created_at 
        FROM user_inquiries 
        WHERE user_id = %s  -- Filter by the logged-in user's ID
        ORDER BY created_at DESC
    """, (current_user.id,))
    inquiries = cursor.fetchall()  # Fetch all inquiries for the logged-in user

    cursor.close()
    conn.close()

    # Convert file size from bytes to KB for display
    for file in uploaded_files + sent_files:
        if file['size']:
            file['size'] = round(file['size'] / (1024 * 1024), 2)   # Convert bytes to KB

    return render_template(
        'userhistory.html',
        uploaded_files=uploaded_files,
        inquiries=inquiries,
        sent_files=sent_files
    )
    
    
#user help desk routes
@app.route('/userhelp', methods=['GET', 'POST'])
@login_required
def userhelp():
    if 'otp_verified' not in session:
        flash('Please verify your OTP to access the help desk.', 'info')
        return redirect(url_for('verify_otp'))

    if request.method == 'POST':
        subject = request.form['subject']
        description = request.form['description']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO user_inquiries (user_id, subject, description)
            VALUES (%s, %s, %s)
        """, (current_user.id, subject, description))
        conn.commit()
        cursor.close()
        conn.close()

        flash('Your inquiry has been submitted successfully.', 'success')
        return redirect(url_for('userhelp'))  # Redirect to refresh the page after form submission

    # Fetch user's inquiries
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, subject, description, status, created_at 
        FROM user_inquiries 
        WHERE user_id = %s
        ORDER BY created_at DESC
    """, (current_user.id,))
    inquiries = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('userhelp.html', inquiries=inquiries)  # Render the template properly


#RENAME FILE FUNCTIONALITY
@app.route('/rename_file/<int:file_id>', methods=['POST'])
@login_required
def rename_file(file_id):
    # Fetch the file from the database
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM files WHERE id = %s", (file_id,))
    file = cursor.fetchone()

    if not file:
        flash('File not found.', 'danger')
        return redirect(url_for('fileshare'))

    # Check if the current user is the owner of the file
    if file['owner_id'] != current_user.id:
        flash('You do not have permission to rename this file.', 'danger')
        return redirect(url_for('fileshare'))

    # Get the new filename from the request
    new_filename = request.form.get('new_filename')
    if not new_filename:
        flash('New filename is required.', 'danger')
        return redirect(url_for('fileshare'))

    # Preserve the file extension
    old_filename = file['filename']
    old_extension = os.path.splitext(old_filename)[1]  # Get the file extension
    new_filename_with_extension = new_filename + old_extension

    # Check if the new filename already exists
    cursor.execute("SELECT id FROM files WHERE filename = %s AND owner_id = %s", (new_filename_with_extension, current_user.id))
    if cursor.fetchone():
        flash('A file with this name already exists.', 'danger')
        return redirect(url_for('fileshare'))

    # Rename the file in the filesystem
    old_file_path = os.path.join('uploads', old_filename)
    new_file_path = os.path.join('uploads', new_filename_with_extension)
    if os.path.exists(old_file_path):
        os.rename(old_file_path, new_file_path)
    else:
        flash('File not found on server.', 'danger')
        return redirect(url_for('fileshare'))

    # Update the filename in the database
    cursor.execute("UPDATE files SET filename = %s WHERE id = %s", (new_filename_with_extension, file_id))
    conn.commit()
    cursor.close()
    conn.close()

    flash('File renamed successfully.', 'success')
    return redirect(url_for('fileshare'))


# DOWNLOAD FILE FUNCTIONALITY
@app.route('/download/<int:file_id>')
@login_required
def download(file_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM files WHERE id = %s", (file_id,))
        file = cursor.fetchone()

        if not file:
            flash('File not found.', 'danger')
            return redirect(url_for('fileshare'))

        # Validate permissions
        is_owner = file['owner_id'] == current_user.id
        is_shared = current_user.username in file['shared_with'].split(',')
        if not (is_owner or is_shared):
            flash('Unauthorized access.', 'danger')
            return redirect(url_for('fileshare'))

        file_path = os.path.join('uploads', file['filename'])
        if not os.path.exists(file_path):
            flash('File not found on server.', 'danger')
            return redirect(url_for('fileshare'))

        with open(file_path, 'rb') as f:
            double_encrypted_data = f.read()

        # Decrypt with AES
        aes_key = file['aes_key']
        decrypted_aes_data = decrypt_aes(double_encrypted_data, aes_key)

        # Decrypt with Fernet
        decrypted_data = cipher.decrypt(decrypted_aes_data)
        
        # Handle ZIP files specially
        if file['filename'].endswith('.zip'):
            response = send_file(
                BytesIO(decrypted_data),
                download_name=file['filename'],
                as_attachment=True,
                mimetype='application/zip'
            )
        else:
            response = send_file(
                BytesIO(decrypted_data),
                download_name=file['filename'],
                as_attachment=True,
                mimetype='application/octet-stream'
            )

        # Check if the file should be deleted after download
        if file['delete_after_download']:
            try:
                os.remove(file_path)
                cursor.execute("DELETE FROM files WHERE id = %s", (file_id,))
                conn.commit()
                flash('File deleted after download.', 'info')
            except Exception as e:
                flash(f'Error deleting file after download: {str(e)}', 'danger')

        return response

    except Exception as e:
        flash(f'Download error: {str(e)}', 'danger')
        return redirect(url_for('fileshare'))
    finally:
        cursor.close()
        conn.close()

# DELETE FILE FUNCTIONALITY
@app.route('/delete_file/<int:file_id>', methods=['POST'])
@login_required
def delete_file(file_id):
    # Verify the file belongs to the current user
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM files WHERE id = %s AND owner_id = %s", (file_id, current_user.id))
    file = cursor.fetchone()
    
    if not file:
        cursor.close()
        conn.close()
        flash('File not found or unauthorized access.', 'danger')
        return redirect(url_for('fileshare'))
    
    # Log the file deletion activity
    log_activity(current_user.id, 'file_deletion', f'File {file[1]} deleted.')

    # Delete the file from the database and filesystem
    file_path = os.path.join('uploads', file[1])  # file[1] is the filename
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
        cursor.execute("DELETE FROM files WHERE id = %s", (file_id,))
        conn.commit()
        flash('File deleted successfully.', 'success')
    except Exception as e:
        flash('Error deleting file.', 'danger')
    finally:
        cursor.close()
        conn.close()
    
    return redirect(url_for('fileshare'))


#SCAN FOR SUSPICIOUS FILE USING MD5 UNIQUE
@app.route('/scan_file', methods=['POST'])
def scan_file():
    data = request.json
    filename = data.get('filename')
    file_md5 = data.get('md5')

    # Check if the file's MD5 hash is in the suspicious hashes list
    if file_md5 in SUSPICIOUS_HASHES:
        return jsonify({"status": "suspicious"})
    else:
        return jsonify({"status": "clean"})


#LOG-OUT FUNCTION FOR USER
@app.route('/logout')
@login_required
def logout():
    session.pop('otp_verified', None)
    logout_user()
    flash('Logged out.', 'info')
    return redirect(url_for('login'))

#CHANGE PASS FOR FIRST TIME LOG-IN
@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        # Fetch the current user's details
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE id = %s", (current_user.id,))
        user = cursor.fetchone()

        if user and bcrypt.check_password_hash(user[0], current_password):
            if new_password == confirm_password:
                # Hash the new password
                hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')

                # Update the password and set password_changed to True
                cursor.execute("""
                    UPDATE users 
                    SET password = %s, password_changed = TRUE 
                    WHERE id = %s
                """, (hashed_password, current_user.id))
                conn.commit()
                cursor.close()
                conn.close()

                flash('Password changed successfully.', 'success')
                return redirect(url_for('verify_otp'))  # Redirect to OTP verification after password change
            else:
                flash('New password and confirm password do not match.', 'danger')
        else:
            flash('Current password is incorrect.', 'danger')

    return render_template('change_password.html')


#FOR VERIFY OTP
@app.route('/verify_otp', methods=['GET', 'POST'])
@login_required
def verify_otp():
    if request.method == 'POST':
        user_otp = request.form['otp']
        if 'otp' in session and user_otp == session['otp']:
            session.pop('otp', None)  # Remove the OTP from the session
            session['otp_verified'] = True  # Set OTP verification status
            flash('Login successfully.', 'success')
            return redirect(url_for('userdashboard'))  # Redirect to the dashboard
        else:
            flash('Invalid OTP.', 'danger')
    
    # Fetch the user's phone number
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Fetch the user's role
    cursor.execute("SELECT role FROM users WHERE id = %s", (current_user.id,))
    role = cursor.fetchone()[0]
    
    # Fetch the phone number based on the role
    if role == 'barangay-captain':
        cursor.execute("SELECT contact_number FROM brgycaptain WHERE user_id = %s", (current_user.id,))
    elif role == 'government-position':
        cursor.execute("SELECT contact_number FROM government_position WHERE user_id = %s", (current_user.id,))
    elif role == 'municipal-employee':
        cursor.execute("SELECT contact_number FROM employee WHERE user_id = %s", (current_user.id,))
    
    phone_number = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    
    # Mask the phone number except for the last 4 digits
    masked_phone_number = '*******' + phone_number[-4:]
    
    return render_template('verify_otp.html', masked_phone_number=masked_phone_number)

# FOR RESEND OTP
@app.route('/resend_otp', methods=['POST'])
@login_required
def resend_otp():
    # Check if 60 seconds have passed since last OTP request
    last_otp_time = session.get('otp_timestamp')
    if last_otp_time and (datetime.now().timestamp() - last_otp_time) < 60:
        return jsonify({'success': False, 'message': 'Please wait 60 seconds before requesting a new OTP'})

    # Fetch user's phone number again
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Fetch the user's role
    cursor.execute("SELECT role FROM users WHERE id = %s", (current_user.id,))
    role = cursor.fetchone()[0]
    
    # Fetch the phone number based on the role
    if role == 'barangay-captain':
        cursor.execute("SELECT contact_number FROM brgycaptain WHERE user_id = %s", (current_user.id,))
    elif role == 'government-position':
        cursor.execute("SELECT contact_number FROM government_position WHERE user_id = %s", (current_user.id,))
    elif role == 'municipal-employee':
        cursor.execute("SELECT contact_number FROM employee WHERE user_id = %s", (current_user.id,))
    
    phone_number = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    # Generate and send new OTP
    new_otp = generate_otp()
    session['otp'] = new_otp
    session['otp_timestamp'] = datetime.now().timestamp()  # Store timestamp
    
    if send_otp_via_sms(phone_number, new_otp):
        return jsonify({'success': True, 'message': 'New OTP has been sent'})
    else:
        return jsonify({'success': False, 'message': 'Failed to send OTP. Please try again.'})

@app.route('/some_protected_route')
@login_required
def some_protected_route():
    if 'otp_verified' not in session:
        flash('Please verify your OTP to access this page.', 'info')
        return redirect(url_for('verify_otp'))
    
#profile picture 
@app.route('/upload_profile_picture', methods=['POST'])
@login_required
def upload_profile_picture():
    if 'profile_picture' not in request.files:
        flash('No file selected', 'danger')
        return redirect(url_for('userprofile'))

    file = request.files['profile_picture']

    if file.filename == '':
        flash('No file selected', 'danger')
        return redirect(url_for('userprofile'))

    if file:
        # Ensure the uploads/profile_pictures directory exists
        if not os.path.exists('uploads/profile_pictures'):
            os.makedirs('uploads/profile_pictures')

        # Encrypt the file
        file_data = file.read()
        encrypted_file = cipher.encrypt(file_data)

        # Save the encrypted file to a folder
        filename = f"profile_{current_user.id}.jpg"
        file_path = os.path.join('uploads/profile_pictures', filename)
        with open(file_path, 'wb') as f:
            f.write(encrypted_file)

        # Update the user's profile picture path in the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET profile_picture = %s WHERE id = %s", (filename, current_user.id))
        conn.commit()
        cursor.close()
        conn.close()

        flash('Profile picture uploaded successfully', 'success')
        return redirect(url_for('userprofile'))

    flash('Failed to upload profile picture', 'danger')
    return redirect(url_for('userprofile'))

@app.route('/profile_picture/<int:user_id>')
@login_required
def profile_picture(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT profile_picture FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result and result[0]:  # Check if profile_picture exists
        file_path = os.path.join('uploads/profile_pictures', result[0])
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                encrypted_file = f.read()
                decrypted_file = cipher.decrypt(encrypted_file)
                return send_file(BytesIO(decrypted_file), mimetype='image/jpeg')

    # Return a default profile picture if no profile picture is set
    return send_file('static/img/pic.png', mimetype='image/png')

@app.route('/remove_profile_picture', methods=['POST'])
@login_required
def remove_profile_picture():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT profile_picture FROM users WHERE id = %s", (current_user.id,))
    result = cursor.fetchone()
    profile_picture = result[0] if result else None

    if profile_picture:
        file_path = os.path.join('uploads/profile_pictures', profile_picture)
        if os.path.exists(file_path):
            os.remove(file_path)

    cursor.execute("UPDATE users SET profile_picture = NULL WHERE id = %s", (current_user.id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'success': True})
    
    # Route to display the messaging interface
@app.route('/messages', methods=['GET'])
@login_required
def messages():
    if 'otp_verified' not in session:
        flash('Please verify your OTP to access the messaging system.', 'info')
        return redirect(url_for('verify_otp'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Fetch all users except the current user for the recipient list
    cursor.execute("""
        SELECT u.id, u.username, u.profile_picture,
               COALESCE(b.first_name, g.first_name, e.first_name) AS first_name,
               COALESCE(b.last_name, g.last_name, e.last_name) AS last_name
        FROM users u
        LEFT JOIN brgycaptain b ON u.id = b.user_id
        LEFT JOIN government_position g ON u.id = g.user_id
        LEFT JOIN employee e ON u.id = e.user_id
        WHERE u.id != %s
    """, (current_user.id,))
    users = cursor.fetchall()

    # Fetch messages for the current user
    cursor.execute("""
        SELECT m.id, m.message, m.created_at, 
               u1.username as sender_username, 
               COALESCE(b1.first_name, g1.first_name, e1.first_name) AS sender_first_name,
               COALESCE(b1.last_name, g1.last_name, e1.last_name) AS sender_last_name,
               u1.profile_picture as sender_profile_picture,
               u2.username as receiver_username, 
               COALESCE(b2.first_name, g2.first_name, e2.first_name) AS receiver_first_name,
               COALESCE(b2.last_name, g2.last_name, e2.last_name) AS receiver_last_name,
               u2.profile_picture as receiver_profile_picture
        FROM messages m
        JOIN users u1 ON m.sender_id = u1.id
        JOIN users u2 ON m.receiver_id = u2.id
        LEFT JOIN brgycaptain b1 ON u1.id = b1.user_id
        LEFT JOIN government_position g1 ON u1.id = g1.user_id
        LEFT JOIN employee e1 ON u1.id = e1.user_id
        LEFT JOIN brgycaptain b2 ON u2.id = b2.user_id
        LEFT JOIN government_position g2 ON u2.id = g2.user_id
        LEFT JOIN employee e2 ON u2.id = e2.user_id
        WHERE m.sender_id = %s OR m.receiver_id = %s
        ORDER BY m.created_at DESC
    """, (current_user.id, current_user.id))
    messages = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('messages.html', users=users, messages=messages)

@app.route('/mark_as_read/<int:message_id>', methods=['POST'])
@login_required
def mark_as_read(message_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE messages 
        SET is_read = TRUE 
        WHERE id = %s AND receiver_id = %s
    """, (message_id, current_user.id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'success': True})

# Route to send a message
@app.route('/send_message', methods=['POST'])
@login_required
def send_message():
    if 'otp_verified' not in session:
        return jsonify({'success': False, 'message': 'Please verify your OTP to send messages.'})

    data = request.json
    receiver_id = data.get('receiver_id')  # Single receiver ID
    message = data.get('message')

    if not receiver_id or not message:
        return jsonify({'success': False, 'message': 'Receiver ID and message are required.'})

    # Encrypt the message using Fernet
    encrypted_message = cipher.encrypt(message.encode('utf-8'))

    # Save the encrypted message to the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO messages (sender_id, receiver_id, message)
        VALUES (%s, %s, %s)
    """, (current_user.id, receiver_id, encrypted_message))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'success': True, 'message': 'Message sent successfully.'})

# Route to fetch messages between the current user and a specific user
@app.route('/get_messages/<int:receiver_id>', methods=['GET'])
@login_required
def get_messages(receiver_id):
    if 'otp_verified' not in session:
        return jsonify({'success': False, 'message': 'Please verify your OTP to view messages.'})

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT m.id, m.message, m.created_at, m.sender_id,
               COALESCE(b1.first_name, g1.first_name, e1.first_name) AS sender_first_name,
               COALESCE(b1.last_name, g1.last_name, e1.last_name) AS sender_last_name,
               u1.profile_picture as sender_profile_picture
        FROM messages m
        LEFT JOIN brgycaptain b1 ON m.sender_id = b1.user_id
        LEFT JOIN government_position g1 ON m.sender_id = g1.user_id
        LEFT JOIN employee e1 ON m.sender_id = e1.user_id
        LEFT JOIN users u1 ON m.sender_id = u1.id
        WHERE (m.sender_id = %s AND m.receiver_id = %s) OR (m.sender_id = %s AND m.receiver_id = %s)
        ORDER BY m.created_at ASC
    """, (current_user.id, receiver_id, receiver_id, current_user.id))
    messages = cursor.fetchall()

    # Decrypt the messages
    for message in messages:
        try:
            decrypted_message = cipher.decrypt(message['message'].encode('utf-8')).decode('utf-8')
            message['message'] = decrypted_message
        except Exception as e:
            print(f"Error decrypting message: {e}")
            message['message'] = "[Unable to decrypt message]"

    cursor.close()
    conn.close()

    return jsonify({'success': True, 'messages': messages})



# Main
if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.mkdir('uploads')
    app.run(debug=True)
    
    
    