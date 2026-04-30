import boto3

def audit_s3():
    print("\n1. Checking S3 Buckets for Public Access...")
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']
    for b in buckets:
        name = b['Name']
        try:
            s3.get_public_access_block(Bucket=name)
            print(f"{name}: Secure")
        except:
            print(f"{name}: NO Public Access Block! Check permissions.")

def audit_iam_mfa():
    print("\n2. Checking IAM Users for MFA...")
    iam = boto3.client('iam')
    users = iam.list_users()['Users']
    for u in users:
        name = u['UserName']
        mfa = iam.list_mfa_devices(UserName=name)['MFADevices']
        if not mfa:
            print(f"User '{name}': MFA DISABLED (High Risk)")
        else:
            print(f"User '{name}': MFA Enabled")

if __name__ == "__main__":
    print("=== AWS Cloud Security Auditor Started ===")
    try:
        audit_s3()
        audit_iam_mfa()
    except Exception as e:
        print(f"Error: {e}")
    print("\n=== Audit Completed ===")