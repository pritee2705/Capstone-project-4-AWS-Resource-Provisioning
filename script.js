// ==========================================
// API GATEWAY URL
// ==========================================

const API_URL =
    "https://9wub3vinj1.execute-api.ap-south-1.amazonaws.com/";


// ==========================================
// COMMON API FUNCTION
// ==========================================

async function callAPI(data) {

    const output =
        document.getElementById("output");

    output.textContent = "Processing...";


    try {

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)

        });


        const result = await response.json();


        output.textContent =
            JSON.stringify(result, null, 2);


    } catch (error) {

        output.textContent =
            "Error: " + error.message;

    }

}


// ==========================================
// LIST S3 BUCKETS
// ==========================================

function listBuckets() {

    callAPI({

        action: "list_buckets"

    });

}


// ==========================================
// CREATE S3 BUCKET
// ==========================================

function createBucket() {

    const bucketName =
        document
            .getElementById("bucketName")
            .value
            .trim();


    if (!bucketName) {

        alert("Please enter bucket name");

        return;

    }


    callAPI({

        action: "create_bucket",

        bucket_name: bucketName

    });

}


// ==========================================
// UPLOAD FILE TO S3
// ==========================================

async function uploadFile() {

    const bucketName =
        document
            .getElementById("uploadBucketName")
            .value
            .trim();


    const fileInput =
        document.getElementById("fileInput");


    const output =
        document.getElementById("output");


    if (!bucketName) {

        alert("Please enter bucket name");

        return;

    }


    if (fileInput.files.length === 0) {

        alert("Please select a file");

        return;

    }


    const file =
        fileInput.files[0];


    output.textContent =
        "Reading file...";


    try {

        const fileContent =
            await file.text();


        output.textContent =
            "Uploading file...";


        const response =
            await fetch(API_URL, {

                method: "POST",

                headers: {

                    "Content-Type":
                        "application/json"

                },

                body: JSON.stringify({

                    action: "upload_file",

                    bucket_name:
                        bucketName,

                    file_name:
                        file.name,

                    file_content:
                        fileContent

                })

            });


        const result =
            await response.json();


        output.textContent =
            JSON.stringify(
                result,
                null,
                2
            );


    } catch (error) {

        output.textContent =
            "Error: " + error.message;

    }

}


// ==========================================
// LIST EC2 INSTANCES
// ==========================================

function listInstances() {

    callAPI({

        action: "list_instances"

    });

}


// ==========================================
// LAUNCH EC2 INSTANCE
// ==========================================

function launchInstance() {

    const amiId =
        document
            .getElementById("amiId")
            .value
            .trim();


    if (!amiId) {

        alert("Please enter AMI ID");

        return;

    }


    callAPI({

        action: "launch_instance",

        ami_id: amiId,

        instance_type: "t3.micro"

    });

}


// ==========================================
// STOP EC2 INSTANCE
// ==========================================

function stopInstance() {

    const instanceId =
        document
            .getElementById("instanceId")
            .value
            .trim();


    if (!instanceId) {

        alert("Please enter Instance ID");

        return;

    }


    callAPI({

        action: "stop_instance",

        instance_id: instanceId

    });

}


// ==========================================
// TERMINATE EC2 INSTANCE
// ==========================================

function terminateInstance() {

    const instanceId =
        document
            .getElementById("instanceId")
            .value
            .trim();


    if (!instanceId) {

        alert("Please enter Instance ID");

        return;

    }


    const confirmed =
        confirm(
            "Are you sure you want to terminate this EC2 instance?"
        );


    if (!confirmed) {

        return;

    }


    callAPI({

        action: "terminate_instance",

        instance_id: instanceId

    });

}


// ==========================================
// CLEAR OUTPUT
// ==========================================

function clearOutput() {

    document.getElementById("output")
        .textContent =
        "Waiting for operation...";

}