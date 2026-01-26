import json
import boto3

bedrock = boto3.client("bedrock-runtime")

def lambda_handler(event, context):
    # 1. Input handle karna hhhhhhh
    if "body" in event and event["body"]:
        try:
            body = json.loads(event["body"])
        except:
            body = event
    else:
        body = event

    prompt = body.get("prompt")

    if not prompt:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "prompt is required"})
        }

    try:
        # 2. Amazon Nova Request Format
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": [{"text": prompt}]
                }
            ],
            "inferenceConfig": {
                "maxTokens": 500,
                "temperature": 0.7
            }
        }

        response = bedrock.invoke_model(
            modelId="amazon.nova-micro-v1:0",
            contentType="application/json",
            accept="application/json",
            body=json.dumps(payload)
        )

        # 3. Response read karna
        response_body = json.loads(response["body"].read())
        
        # Nova ka response extract karna
        reply = response_body["output"]["message"]["content"][0]["text"]

        return {
            "statusCode": 200,
            "body": json.dumps({"response": reply})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
