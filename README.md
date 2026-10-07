# AWS Resource Automation

## 1. Project Title and Objective

### Project Title

**AWS Resource Automation using Python, Boto3, AWS Lambda, API Gateway, S3 and EC2**

### Objective

The objective of this project is to automate common AWS resource management operations instead of performing them manually through the AWS Management Console.

The project provides **two separate interfaces**:

1. **Web-based AWS Resource Automation**

   * HTML, CSS and JavaScript frontend
   * API Gateway HTTP API
   * AWS Lambda
   * Python Boto3
   * Amazon S3 and Amazon EC2

2. **Command-Line AWS Resource Automation**

   * Python CLI application
   * Boto3
   * Direct interaction with Amazon S3 and Amazon EC2

The application supports operations such as:

* List S3 buckets
* Create S3 buckets
* Upload files to S3
* List EC2 instances
* Launch EC2 instances
* Stop EC2 instances
* Terminate EC2 instances

---

# 2. AWS Services Used

| AWS Service            | Purpose                                                   |
| ---------------------- | --------------------------------------------------------- |
| **AWS Lambda**         | Executes Python automation logic without managing servers |
| **Amazon API Gateway** | Provides HTTP API endpoints for the web application       |
| **Amazon S3**          | Used for bucket management and file uploads               |
| **Amazon EC2**         | Used for instance management                              |
| **AWS IAM**            | Provides permissions and secure access to AWS resources   |
| **AWS CloudWatch**     | Can be used for Lambda execution logs and monitoring      |
| **AWS STS**            | Used by the CLI to verify AWS credentials and identity    |
| **Boto3**              | Python SDK used to interact with AWS services             |

---

# 3. Architecture / Workflow

## 3.1 Web Application Architecture

```text
                   USER
                     |
                     v
          +----------------------+
          |   Web Browser        |
          | HTML/CSS/JavaScript  |
          +----------+-----------+
                     |
                     | HTTP POST
                     v
          +----------------------+
          |   API Gateway        |
          |     HTTP API         |
          +----------+-----------+
                     |
                     v
          +----------------------+
          |    AWS Lambda        |
          | Python + Boto3       |
          +----------+-----------+
                     |
              +------+------+
              |             |
              v             v
       +-------------+ +-------------+
       | Amazon S3   | | Amazon EC2  |
       +-------------+ +-------------+
```

### Web Application Workflow

```text
User selects an operation
          |
          v
JavaScript sends JSON request
          |
          v
API Gateway receives request
          |
          v
Lambda processes the request
          |
          v
Boto3 calls AWS service
          |
          v
S3 / EC2 performs operation
          |
          v
Lambda returns response
          |
          v
Result displayed in browser
```

---

## 3.2 Command-Line Architecture

The CLI is implemented as a **separate module** and does not depend on the web application.

```text
       User
        |
        v
+---------------------+
| Python CLI          |
| aws_cli.py          |
+----------+----------+
           |
           | Boto3
           v
     +-----+------+
     |            |
     v            v
+---------+   +---------+
|   S3    |   |   EC2   |
+---------+   +---------+
```

### CLI Workflow

```text
Run aws_cli.py
      |
      v
AWS credentials verified
      |
      v
Command-line menu displayed
      |
      v
User selects operation
      |
      v
Python function executes
      |
      v
Boto3 calls AWS
      |
      v
Result displayed in terminal
```

---

# 4. Implementation Steps

## Step 1 — Create IAM Role

An IAM role was created for the AWS Lambda function.

The role provides permissions required to interact with:

* Amazon S3
* Amazon EC2

The required permissions include operations such as:

```text
s3:ListAllMyBuckets
s3:GetBucketLocation
s3:CreateBucket
s3:PutObject
s3:GetObject
```

EC2 permissions were also configured for:

```text
DescribeInstances
RunInstances
StopInstances
TerminateInstances
```

---

## Step 2 — Create AWS Lambda Function

A Python Lambda function named:

```text
AWSResourceAutomation
```

was created.

The Lambda function uses:

```text
Python
Boto3
```

to perform AWS resource operations.

The Lambda function accepts an `action` value to determine which operation should be performed.

Example:

```json
{
    "action": "list_buckets"
}
```

---

## Step 3 — Implement S3 Operations

The Lambda function supports:

### List Buckets

```json
{
    "action": "list_buckets"
}
```

### Create Bucket

```json
{
    "action": "create_bucket",
    "bucket_name": "example-bucket-name"
}
```

### Upload File

```json
{
    "action": "upload_file",
    "bucket_name": "example-bucket-name",
    "file_name": "example.txt",
    "file_content": "Hello AWS"
}
```

---

## Step 4 — Implement EC2 Operations

The Lambda function supports:

### List Instances

```json
{
    "action": "list_instances"
}
```

### Launch Instance

```json
{
    "action": "launch_instance",
    "ami_id": "ami-xxxxxxxxxxxxxxxxx",
    "instance_type": "t3.micro"
}
```

### Stop Instance

```json
{
    "action": "stop_instance",
    "instance_id": "i-xxxxxxxxxxxxxxxxx"
}
```

### Terminate Instance

```json
{
    "action": "terminate_instance",
    "instance_id": "i-xxxxxxxxxxxxxxxxx"
}
```

---

## Step 5 — Create API Gateway

An HTTP API was created using Amazon API Gateway.

The API forwards requests to:

```text
AWSResourceAutomation Lambda
```

The web application sends POST requests to the API Gateway endpoint.

Example:

```text
POST / 
```

with a JSON request body.

---

## Step 6 — Configure CORS

CORS was configured to allow the browser-based frontend to communicate with API Gateway.

The configuration includes:

```text
Allowed Origin:
*

Allowed Header:
content-type

Allowed Methods:
POST
OPTIONS
```

---

## Step 7 — Test API Using Postman

All major API operations were tested using Postman before connecting the frontend.

The following operations were tested:

```text
1. List S3 Buckets
2. Create S3 Bucket
3. Upload File to S3
4. List EC2 Instances
5. Launch EC2 Instance
6. Stop EC2 Instance
7. Terminate EC2 Instance
```

---

## Step 8 — Develop Web Frontend

The frontend was developed using:

```text
HTML
CSS
JavaScript
```

The frontend provides separate sections for:

* S3 Management
* EC2 Management
* Operation Results

Project structure:

```text
AWS-Resource-Automation/
│
├── index.html
├── style.css
├── script.js
│
└── cli/
    └── aws_cli.py
```

---

## Step 9 — Connect Frontend to API Gateway

JavaScript uses the Fetch API to send requests to API Gateway.

Example:

```javascript
fetch(API_URL, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        action: "list_buckets"
    })
});
```

The Lambda response is displayed in the Operation Result section.

---

## Step 10 — Add Operation Status

The frontend displays operation status such as:

```text
Ready
Processing...
Success
Error
```

This improves the user experience by allowing the user to understand the current state of an AWS operation.

---

# 5. Command-Line Module

A separate CLI module was created inside:

```text
cli/aws_cli.py
```

The CLI provides the following menu:

```text
==================================================
        AWS RESOURCE AUTOMATION CLI
==================================================
1. List S3 Buckets
2. Create S3 Bucket
3. Upload File to S3
4. List EC2 Instances
5. Launch EC2 Instance
6. Stop EC2 Instance
7. Terminate EC2 Instance
8. Exit
==================================================
```

The CLI uses:

```text
Python
Boto3
AWS IAM credentials
```

Unlike the web application, the CLI communicates directly with AWS through Boto3.

---

# 6. Screenshots of Important Configurations and Results

## Screenshot 1 — Project Folder Structure


```text
screenshots/01-project-structure.png
```

---

## Screenshot 2 — IAM Role


```text
screenshots/02-iam-role.png
```

---

## Screenshot 3 — Lambda Function


```text
screenshots/03-lambda-function.png
```

---

## Screenshot 4 — Lambda Successful Test


```json
{
    "action": "list_buckets"
}
```


```text
screenshots/04-lambda-test.png
```

---

## Screenshot 5 — API Gateway


```text
screenshots/05-api-gateway.png
```

---

## Screenshot 6 — Postman API Test


```text
List S3 Buckets
```


```text
screenshots/06-postman-test.png
```

---

## Screenshot 7 — S3 Bucket Created


```text
screenshots/07-s3-bucket.png
```

---

## Screenshot 8 — Web Application


```text
screenshots/08-web-application.png
```

---

## Screenshot 9 — Web Application Result


```text
List EC2 Instances
```


```text
screenshots/09-web-operation-result.png
```

---

---

## Screenshot 10 — CLI EC2 Operation

```text
screenshots/10-cli-ec2-operation.png
```

---

# 7. How to Run or Deploy the Project

## Prerequisites

Install:

* Python 3.x
* AWS CLI
* Boto3
* AWS account
* IAM user/role with required permissions
* Web browser
* Postman (optional, for API testing)

---

## Configure AWS CLI Credentials

Configure AWS credentials locally:

```bash
aws configure
```

Enter:

```text
AWS Access Key ID
AWS Secret Access Key
Default region: ap-south-1
Default output format: json
```

Verify the credentials:

```bash
aws sts get-caller-identity
```

---

## Install Boto3

Run:

```bash
pip install boto3
```

---

## Run the CLI Module

Navigate to:

```bash
cd AWS-Resource-Automation\cli
```

Run:

```bash
python aws_cli.py
```

The command-line menu will appear.

---

## Run the Web Application

Open:

```text
index.html
```

in a web browser.

Before running the frontend, update the API Gateway URL in:

```text
script.js
```

Replace:

```javascript
const API_URL =
    "https://YOUR-API-ID.execute-api.ap-south-1.amazonaws.com/";
```

with the actual API Gateway endpoint.

The frontend can then be used to manage S3 and EC2 resources.

---

# 8. Project Structure

```text
AWS-Resource-Automation/
│
├── index.html
├── style.css
├── script.js
│
├── cli/
│   └── aws_cli.py
│
└── screenshots/
    ├── 01-project-structure.png
    ├── 02-iam-role.png
    ├── 03-lambda-function.png
    ├── 04-lambda-test.png
    ├── 05-api-gateway.png
    ├── 06-postman-test.png
    ├── 07-s3-bucket.png
    ├── 08-web-application.png
    ├── 09-web-operation-result.png
    ├── 10-cli-menu.png
    ├── 11-cli-s3-operation.png
    └── 12-cli-ec2-operation.png
```

---

# 9. Key Learnings

Through this project, the following concepts were implemented and understood:

### AWS Automation

Learned how to automate AWS resource management using Python and Boto3 instead of manually performing operations through the AWS Console.

### AWS Lambda

Learned how to execute Python automation code using a serverless AWS Lambda function.

### API Gateway

Learned how to expose Lambda functionality through HTTP APIs.

### Amazon S3

Implemented automated:

* Bucket listing
* Bucket creation
* File upload

### Amazon EC2

Implemented automated:

* Instance listing
* Instance launching
* Instance stopping
* Instance termination

### IAM

Learned how IAM roles and permissions control access to AWS resources.

### Boto3

Learned how Python applications communicate programmatically with AWS services using the AWS SDK.

### REST API Integration

Learned how a JavaScript frontend communicates with a serverless backend through API Gateway.

### CORS

Learned how to configure CORS so that browser-based applications can communicate with API Gateway.

### Command-Line Automation

Built a separate Python CLI module that allows users to select AWS operations through a numbered menu.

### Error Handling

Implemented exception handling so that AWS errors are displayed to the user instead of causing the application to terminate unexpectedly.

### Serverless Architecture

Gained practical experience designing a serverless architecture using:

```text
API Gateway
      ↓
Lambda
      ↓
Boto3
      ↓
S3 / EC2
```

---

# 10. Conclusion

The **AWS Resource Automation** project demonstrates how common AWS resource management tasks can be automated through both a web interface and a command-line application.

The web application provides a user-friendly interface for AWS resource management, while the separate CLI module provides a lightweight terminal-based automation solution.

This project demonstrates practical knowledge of:

```text
Python
Boto3
AWS Lambda
API Gateway
Amazon S3
Amazon EC2
IAM
JavaScript
REST APIs
CORS
Serverless Architecture
CLI Automation
```

It provides a foundation for extending the system with additional AWS services such as:

```text
DynamoDB
RDS
CloudWatch
SNS
VPC
ECS
CloudFormation
```
