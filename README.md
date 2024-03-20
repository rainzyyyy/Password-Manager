# Password-Manager :inbox_tray:

This is a simple Python script allows users to add and retrieve passwords. It utilizes the cryptography library to encrypt and decrypt passwords using Fernet symmetric encryption.

<h3>Usage:</h3>

1. **Setup** <br>
Before running the script, make sure you have installed the required dependencies. You can install them using pip: **pip install cryptography**

2. **Running the Script** <br>
Run the script 'password_manager.py'.

3. **Instructions**
<ul>
  <li>Upon running the script, you'll be prompted to enter your master password. The default master password for testing purposes is "hello".</li>
  <li>You can then choose to add a new password or retrieve an existing one.</li>
  <li>When adding a password, enter the account name and password. The password will be encrypted and stored in the 'password.txt' file.</li>
  <li>When retrieving a password, the script will decrypt and display the stored password.</li>
</ul>

<h3>Note:</h3>
This script is for demostration and testing purposes only. DO NOT USE it to store real passwords.
