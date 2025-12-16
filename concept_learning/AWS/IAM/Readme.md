## IAM

1. User group : Identity to a group of users, also have permissions attached. Roles are not attached to user groups, users in a group are attached to the permission policies of the group.
2. Roles: Identity to a Permission, accessed by users, application and services. 

Roles are never directly attached to a user. Permission can eb attached to the user

=> To allow users groups to get assigned to a role:
    a. Grant sts:AssumeRole policy to get that role assigned
    b. User in the policy can then assume that role

=> To assign a role with permission to a user:
    - First create a role with permssion to EC2(example)
    - Add policy to user to assum role sts:AssumeRole, in ehich you mention the role name
    - then the user in his iam account can use the switch role which prvides temp credentials to access the resource by switching to assume that role.

3. Root account : Key account , by default has all roles(Uses email as user id)
4. User Account : Only will have login access, by default no roles(Uses Name + AWS ID)

5. IAM Roles arfe designed to be assigned permission for temporary bais where as User groups have permenant access to the permission

6. There are 2 types of policies : Identity based, Resource based(for resources to access lie S3 ). 

7. IAM Roles for Applications (Service Accounts)

    Applications running outside AWS:
        Use AWS STS (AssumeRoleWithWebIdentity, AssumeRoleWithSAML, or AssumeRole) to get temporary credentials.
    Example: A mobile app or on-premises server can authenticate via OIDC or SAML and assume a role.

    Applications running inside AWS (EC2, Lambda, ECS, etc.):
        Assign an IAM role to the compute resource.
        The application automatically gets temporary credentials via the instance metadata service.


    Resource-Based Policies

    Some AWS resources (like S3 buckets, Lambda functions, SQS queues) support resource-based policies.
        You can grant access to:
        AWS accounts
        IAM roles
        Federated users
        AWS services

## AUTHETICATION

1. To management console, Username, psw, MFA
2. Through API (programmatic access): Access key ID, Secret Access Key

