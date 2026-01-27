# Serverless LLM Inference API with Automated CI/CD

### 🚀 Project Overview
This project demonstrates a production-ready serverless API that leverages **Amazon Bedrock** for LLM inference. It is built with a focus on **Infrastructure as Code (IaC)**, automation, and performance, featuring a fully automated deployment pipeline.

### 🏗️ Architecture
The infrastructure is managed via **Terraform** and consists of the following components:
* **Trigger:** AWS Lambda Function URL providing a direct HTTPS endpoint.
* **Compute:** AWS Lambda (Python 3.12) optimized for inference tasks.
* **AI Engine:** Amazon Bedrock.
* **Model:** **Amazon Nova Micro (v1.0)**, selected for high-speed, low-latency text generation.
* **CI/CD:** GitHub Actions for automated code deployment to the cloud.



### 📂 Repository Structure
* **`/.github/workflows/`**: Contains `pipeline.yml` for the automated CI/CD pipeline.
* **`/terraform/`**: Contains IaC files (`main.tf`, `input.tf`, `output.tf`) to provision AWS resources.
* **`lambda_function.py`**: Core Python logic for interacting with the Amazon Bedrock Runtime API.
* **`README.md`**: Project documentation and testing instructions.

### 🛠️ Engineering Highlights
1. **Infrastructure as Code (IaC):** Utilized Terraform to ensure the environment is reproducible, version-controlled, and easily scalable.
2. **Automated CI/CD:** Implemented a GitHub Actions pipeline that automatically packages the Python code and updates the Lambda function (`dpl`) on every push to the `main` branch.
3. **Modern LLM Integration:** Utilized the **Amazon Nova** model family via the Bedrock Standard Messages API, offering superior performance-to-cost ratios.
4. **Security First:** Configured IAM roles with the **Principle of Least Privilege**, granting the Lambda function only the necessary permissions to invoke Bedrock models and log to CloudWatch.
5. **Simplicity:** Leveraged **Lambda Function URLs** instead of API Gateway to fulfill the requirement for a minimal, single-endpoint architecture.

### 🧪 How to Test
The API is exposed via a public Lambda Function URL. You can use **Postman** or `curl` to send a POST request.

**Live Endpoint:** `https://cl6w5bhwx56uzlo2eljfeeczre0iszre.lambda-url.us-east-1.on.aws/`

**Sample Request (cURL):**
```bash
curl -X POST [https://cl6w5bhwx56uzlo2eljfeeczre0iszre.lambda-url.us-east-1.on.aws/](https://cl6w5bhwx56uzlo2eljfeeczre0iszre.lambda-url.us-east-1.on.aws/) \
     -H "Content-Type: application/json" \
     -d '{"prompt": "What are the benefits of using Infrastructure as Code?"}'
