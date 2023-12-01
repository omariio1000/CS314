# CS314 - Chocaholics Anonymous

## Manager Mode

### Users and Passwords

Default manager usernames and passwords:
  * admin: "admin"
  * manager: "manager"

New admin users can be created in admin mode, and passwords can be changed.

### Functions

**Add/Edit/Remove Member**

Can add, edit, or remove a member. All inputs are checked for errors. Can only add or change member ID if the ID isn't taken by another member.

**Add/Edit/Remove Provider**

Can add, edit, or remove a provider. All inputs are checked for errors. Can only add or change provider ID if the ID isn't taken by another provider.

**Add/Edit/Remove Service**

Can add, edit, or remove a service. All inputs are checked for errors. Can only add or change service code if the code isn't taken by another service.

**Add/Edit/Remove Record**

Can add, edit, or remove a record. All inputs are checked for errors. 

**Generate Reports**

Generate three types of reports:
  * Provider summary report  
  * Member summary report
  * Provider EFT report

These reports are collected a week from the date when the report is generated.

**Change Account Password**

Change the password for the admin that is currently logged in. Allows user to view the password before deciding whether or not to change it.

**Add New Admin**

Add a new admin and set their password.

**Change Provider Password**

Change the password for any provider. Allows user to view the password before deciding whether or not to change it.

## Provider Mode

### Default Passwords
All newly created providers have default password of "password". These can be changed by an admin or a provider.

### Functions

**Verify member ID**

Print the status of a member, if the ID exists. Otherwise warn user that ID doesn't exist.

**Print Records**

Print all records the provider has made, that are stored in the filesystem.

**Create a record**

Create a service record and store it in the filesystem.

**Displaying Services**

Display a list of services offered and their descriptions, codes, and cost.

**Change  password**

Change provider password. Allows provider to view it before defciding whether or not to change it.

## File Formatting
Files are created by the program automatically, but in case of fixing corrupted files, the format is provided here.

### Member Files
There are 7 lines in a member file. The name of the file is the member ID followed by the extension `.mem`. The lines contain the following information:

  1. Member name
  2. Member ID
  3. Address
  4. City
  5. State
  6. Zip Code
  7. Status (0 for Suspended, 1 for Validated)

### Provider Files
There are 8 lines in a provider file. The name of the file is the provider ID followed by the extension `.prov`. The lines contain the following information:

  1. Provider name
  2. Provider ID
  3. Address
  4. City
  5. State
  6. Zip Code
  7. Status (always 0, unused)
  8. Comma separated list of service codes offered

### Service Files
There are 4 lines in a service file. The name of the file is the service code followed by the extension `.svc`. The lines contain the following information:

  1. Service code
  2. Service name
  3. Description
  4. Cost

### Record Files
There are 5 or 6 lines in a record file. The name of the file is the date it was created (YYYY_MM_DD_HH_MM_SS) followed by the extension `.rec`. The lines contain the following information:

  1. Date of service (YYYY_MM_DD)
  2. Provider ID
  3. Member ID
  4. Service Code
  5. Bill
  6. Comments (empty line for no comments)

### Password Files
There are two files storing passwords, one for providers and one for managers. They are stored in `providers.pass` and `managers.pass` respectively. Each line of these files contains a username and password. The username for providers is their provider ID. The format of each line is `username:password`.