import boto3


# ==========================================
# AWS CLIENTS
# ==========================================

REGION = "ap-south-1"

s3 = boto3.client(
    "s3",
    region_name=REGION
)

ec2 = boto3.client(
    "ec2",
    region_name=REGION
)


# ==========================================
# DISPLAY MENU
# ==========================================

def show_menu():

    print("\n")
    print("=" * 50)
    print("        AWS RESOURCE AUTOMATION CLI")
    print("=" * 50)

    print("1. List S3 Buckets")
    print("2. Create S3 Bucket")
    print("3. Upload File to S3")
    print("4. List EC2 Instances")
    print("5. Launch EC2 Instance")
    print("6. Stop EC2 Instance")
    print("7. Terminate EC2 Instance")
    print("8. Exit")

    print("=" * 50)


# ==========================================
# 1. LIST S3 BUCKETS
# ==========================================

def list_buckets():

    print("\nFetching S3 buckets...")

    try:

        response = s3.list_buckets()

        buckets = response.get("Buckets", [])


        if not buckets:

            print("\nNo S3 buckets found.")

            return


        print("\nS3 Buckets:")
        print("-" * 50)


        for index, bucket in enumerate(
            buckets,
            start=1
        ):

            print(
                f"{index}. {bucket['Name']}"
            )


    except Exception as e:

        print("\nFailed to list S3 buckets.")

        print("Error:", e)


# ==========================================
# 2. CREATE S3 BUCKET
# ==========================================

def create_bucket():

    print("\nCreate S3 Bucket")

    bucket_name = input(
        "Enter bucket name: "
    ).strip()


    if not bucket_name:

        print(
            "\nBucket name cannot be empty."
        )

        return


    try:

        s3.create_bucket(

            Bucket=bucket_name,

            CreateBucketConfiguration={
                "LocationConstraint": REGION
            }

        )


        print(
            "\nS3 bucket created successfully!"
        )

        print(
            "Bucket:",
            bucket_name
        )


    except Exception as e:

        print(
            "\nFailed to create S3 bucket."
        )

        print(
            "Error:",
            e
        )


# ==========================================
# 3. UPLOAD FILE TO S3
# ==========================================

def upload_file():

    print("\nUpload File to S3")


    bucket_name = input(
        "Enter bucket name: "
    ).strip()


    if not bucket_name:

        print(
            "\nBucket name cannot be empty."
        )

        return


    file_path = input(
        "Enter local file path: "
    ).strip()


    if not file_path:

        print(
            "\nFile path cannot be empty."
        )

        return


    try:

        s3.upload_file(

            file_path,

            bucket_name,

            file_path.split("\\")[-1]

        )


        print(
            "\nFile uploaded successfully!"
        )

        print(
            "Bucket:",
            bucket_name
        )

        print(
            "File:",
            file_path.split("\\")[-1]
        )


    except Exception as e:

        print(
            "\nFailed to upload file."
        )

        print(
            "Error:",
            e
        )


# ==========================================
# 4. LIST EC2 INSTANCES
# ==========================================

def list_instances():

    print("\nFetching EC2 instances...")

    try:

        response = ec2.describe_instances()

        instances = []


        for reservation in response.get(
            "Reservations",
            []
        ):

            for instance in reservation.get(
                "Instances",
                []
            ):

                instances.append(instance)


        if not instances:

            print(
                "\nNo EC2 instances found."
            )

            return


        print("\nEC2 Instances:")
        print("-" * 80)


        for index, instance in enumerate(
            instances,
            start=1
        ):

            instance_id = instance.get(
                "InstanceId",
                "N/A"
            )

            state = instance.get(
                "State",
                {}
            ).get(
                "Name",
                "N/A"
            )

            instance_type = instance.get(
                "InstanceType",
                "N/A"
            )

            private_ip = instance.get(
                "PrivateIpAddress",
                "N/A"
            )

            public_ip = instance.get(
                "PublicIpAddress",
                "N/A"
            )


            print(
                f"\n{index}. Instance ID : {instance_id}"
            )

            print(
                f"   State         : {state}"
            )

            print(
                f"   Instance Type : {instance_type}"
            )

            print(
                f"   Private IP    : {private_ip}"
            )

            print(
                f"   Public IP     : {public_ip}"
            )


    except Exception as e:

        print(
            "\nFailed to list EC2 instances."
        )

        print(
            "Error:",
            e
        )


# ==========================================
# 5. LAUNCH EC2 INSTANCE
# ==========================================

def launch_instance():

    print("\nLaunch EC2 Instance")


    ami_id = input(
        "Enter AMI ID: "
    ).strip()


    if not ami_id:

        print(
            "\nAMI ID cannot be empty."
        )

        return


    instance_type = input(
        "Enter instance type [t3.micro]: "
    ).strip()


    if not instance_type:

        instance_type = "t3.micro"


    try:

        response = ec2.run_instances(

            ImageId=ami_id,

            InstanceType=instance_type,

            MinCount=1,

            MaxCount=1

        )


        instance = response[
            "Instances"
        ][0]


        instance_id = instance[
            "InstanceId"
        ]


        print(
            "\nEC2 instance launched successfully!"
        )

        print(
            "Instance ID:",
            instance_id
        )

        print(
            "Instance Type:",
            instance_type
        )

        print(
            "AMI ID:",
            ami_id
        )


    except Exception as e:

        print(
            "\nFailed to launch EC2 instance."
        )

        print(
            "Error:",
            e
        )


# ==========================================
# 6. STOP EC2 INSTANCE
# ==========================================

def stop_instance():

    print("\nStop EC2 Instance")


    instance_id = input(
        "Enter Instance ID: "
    ).strip()


    if not instance_id:

        print(
            "\nInstance ID cannot be empty."
        )

        return


    try:

        response = ec2.stop_instances(

            InstanceIds=[
                instance_id
            ]

        )


        print(
            "\nEC2 instance stop requested successfully!"
        )


        for instance in response.get(
            "StoppingInstances",
            []
        ):

            print(
                "Instance ID:",
                instance["InstanceId"]
            )

            print(
                "Previous State:",
                instance[
                    "PreviousState"
                ]["Name"]
            )

            print(
                "Current State:",
                instance[
                    "CurrentState"
                ]["Name"]
            )


    except Exception as e:

        print(
            "\nFailed to stop EC2 instance."
        )

        print(
            "Error:",
            e
        )


# ==========================================
# 7. TERMINATE EC2 INSTANCE
# ==========================================

def terminate_instance():

    print("\nTerminate EC2 Instance")


    instance_id = input(
        "Enter Instance ID: "
    ).strip()


    if not instance_id:

        print(
            "\nInstance ID cannot be empty."
        )

        return


    confirmation = input(
        f"Are you sure you want to terminate "
        f"{instance_id}? (yes/no): "
    ).strip().lower()


    if confirmation != "yes":

        print(
            "\nTermination cancelled."
        )

        return


    try:

        response = ec2.terminate_instances(

            InstanceIds=[
                instance_id
            ]

        )


        print(
            "\nEC2 instance termination requested successfully!"
        )


        for instance in response.get(
            "TerminatingInstances",
            []
        ):

            print(
                "Instance ID:",
                instance["InstanceId"]
            )

            print(
                "Previous State:",
                instance[
                    "PreviousState"
                ]["Name"]
            )

            print(
                "Current State:",
                instance[
                    "CurrentState"
                ]["Name"]
            )


    except Exception as e:

        print(
            "\nFailed to terminate EC2 instance."
        )

        print(
            "Error:",
            e
        )


# ==========================================
# MAIN MENU
# ==========================================

def main():

    print("\nConnecting to AWS...")

    try:

        # Test AWS authentication

        sts = boto3.client(
            "sts",
            region_name=REGION
        )

        identity = sts.get_caller_identity()

        print(
            "AWS connection successful!"
        )

        print(
            "Account:",
            identity["Account"]
        )


    except Exception as e:

        print(
            "\nAWS connection failed!"
        )

        print(
            "Error:",
            e
        )

        return


    while True:

        show_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()


        if choice == "1":

            list_buckets()


        elif choice == "2":

            create_bucket()


        elif choice == "3":

            upload_file()


        elif choice == "4":

            list_instances()


        elif choice == "5":

            launch_instance()


        elif choice == "6":

            stop_instance()


        elif choice == "7":

            terminate_instance()


        elif choice == "8":

            print(
                "\nExiting AWS Resource Automation CLI..."
            )

            break


        else:

            print(
                "\nInvalid choice."
            )

            print(
                "Please select a number between 1 and 8."
            )


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":

    main()