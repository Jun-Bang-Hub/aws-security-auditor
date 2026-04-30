### **AWS Security Audit Script**

I made this script to automate some basic security checks. 

Instead of checking the console manually, I used **Python and Boto3** to quickly find common security risks.

#### **Main Features**
- **S3 Audit**: Checks if buckets have "Public Access Block" enabled to prevent data leaks.
- **IAM Audit**: Scans all users to see if **MFA** is enabled.

#### **How to Use**
1. Install boto3: `pip install boto3`
2. Set up AWS credentials: `aws configure`
3. Run the script: `python aws_security_auditor.py`

#### **Example Output**
```text
=== AWS Cloud Security Auditor Started ===
1. Checking S3 Buckets for Public Access...
2. Checking IAM Users for MFA...
User 'Hyojun': MFA DISABLED (High Risk)
=== Audit Completed ===
```
