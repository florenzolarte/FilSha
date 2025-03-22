from flask import Flask, render_template, request, redirect, url_for, flash, send_file, session, jsonify
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from io import BytesIO
import mysql.connector
import os
import hashlib
import random
import requests
import string
from flask_mail import Mail, Message
import os
from datetime import datetime, timedelta
import zipfile
from flask_socketio import SocketIO, emit
import json
from datetime import timedelta
import tempfile
import shutil
#from flask_wtf.csrf import CSRFProtect, generate_csrf //work in progress