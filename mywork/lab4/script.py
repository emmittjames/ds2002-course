import boto3
import requests
from urllib.parse import urlparse

def fetch_and_save_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

def upload_to_s3_and_generate_presigned_url(bucket_name, file_path, expires_in):
    s3 = boto3.client('s3', region_name='us-east-1')

    with open(file_path, 'rb') as file:
        resp = s3.put_object(
            Body=file,
            Bucket=bucket_name,
            Key=file_path,
            ACL = 'public-read',
        )

    print(resp)

    presigned_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': file_path},
        ExpiresIn=expires_in,
    )

    return presigned_url

bucket_name = 'ds2002-gwu8ek'
url = 'https://api.dsi.virginia.edu/sites/default/files/styles/scale_lg/public/2023-05/rotunda_march_2018_ss_header_3-2_1%20%281%29.jpg'
file_path = 'rotunda.jpg'
expires_in = 604800 

fetch_and_save_file(url, file_path)

presigned_url = upload_to_s3_and_generate_presigned_url(bucket_name, file_path, expires_in)

print("Presigned URL:", presigned_url)

#https://ds2002-gwu8ek.s3.amazonaws.com/rotunda.jpg?AWSAccessKeyId=ASIATCKAQDQ64MVFJ752&Signature=FSrVz9u1S%2FA8uuQToaGmABjUm68%3D&x-amz-security-token=FwoGZXIvYXdzEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDFvmDGkre8%2FEhLYI7SLEAbTs7NnEuf4hWutYjczQhTd6Z5qPwVuhxP8Kg8hC0nEJqLsHk8Gv0MplDpKl72fK2O1Mbq%2FJoQSv3Zh6NLFt8MDvh8wyC3wVh18b%2F0IyYDlEWyuTfqFcQED%2FyfK44PciCoj2sUGUtwuxY2fqhISjSydSJ8FJQDndaTPuP%2B0gX4dC6cHrFcyn7vi0YQc6RI0TZSMFhu7tS4uQhVNlkEDApo0sQh3WWuX%2BqdfNSVXdhXkF7L7hT3b14c5lXVDMMRzQ1R0yz9co1aOlrwYyLb57qgROEDbVf%2BOH3i2ijI%2BGVRkhPPZn3FRHQ9iGhX9LekGjSJiaEvJVi6CCTg%3D%3D&Expires=1710394542
