#!/usr/bin/python3

# pip install boto3
import boto3
import rekogCreds as creds

def awsConnection():
    print('RekognitionV1 || AwsConnection: Establishing connection with AWS')
    session = boto3.Session(
        aws_access_key_id=creds.aws_access_key_id,
        aws_secret_access_key=creds.aws_secret_access_key,
        aws_session_token=creds.aws_session_token,
        region_name=creds.region
    )
    s3 = session.resource('s3')
    rekognition = session.client('rekognition')
    print('RekognitionV1 || AwsConnection: Connection established with AWS')
    return s3, rekognition

def uploadS3File(s3, imagePath, imageName):
    print('RekognitionV1 || UploadS3File: Uploading image to AWS Bucket')
    s3.Object(creds.bucket, imageName).upload_file(imagePath)
    print('RekognitionV1 || UploadS3File: File uploaded to AWS Bucket')

def lblsAndBrandsDetection(rekog, fileName):
    print('RekognitionV1 || LblsAndBrandsDetection: Detecting product')
    lblResponse = rekog.detect_labels(Image={'S3Object': {'Bucket': creds.bucket, 'Name': fileName}})
    labels = lblResponse['Labels']
    brnResponse = rekog.detect_text(Image={'S3Object': {'Bucket': creds.bucket, 'Name': fileName}})
    brands = [text['DetectedText'] for text in brnResponse['TextDetections'] if text['Type'] == 'LINE']
    print('RekognitionV1 || LblsAndBrandsDetection: Product detected')

    return labels, brands

def productSearch(label, brand):
    print('RekognitionV1 || ProductSearch: Searching product online')
    base_url = "https://www.amazon.com/s?k="
    searchQuery = '+'.join(label.split()) + '+' + '+'.join(brand.split())
    search_url = base_url + searchQuery
    return search_url

if __name__ == '__main__':
    s3, rekog = awsConnection()
    uploadS3File(s3=s3, imagePath='TEMPFILES/images/productImg.png', imageName='productImg.png')
    labels, brands = lblsAndBrandsDetection(rekog=rekog, fileName='productImg.png')
    if labels and brands:
        for label in labels:
            for brand in brands:
                amazon_url = productSearch(label['Name'], brand)
                print(f'Url: {amazon_url}')