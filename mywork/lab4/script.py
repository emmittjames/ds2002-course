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

#https://ds2002-gwu8ek.s3.amazonaws.com/rotunda.jpg?AWSAccessKeyId=ASIATCKAQDQ6VJAWGMPC&Signature=%2FW4UjdynPmDFeJP2FebMS9fBflY%3D&x-amz-security-token=FwoGZXIvYXdzEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDKZfIhYo%2Bo6apTgghyLEAbRd0zOZRZCz8NFGTp8FJJuI%2BjAoD9%2BgUrrbOZ6UG6BvMHcyjzFCZZNu%2B3NoqTiayEwWjhxXlvSMLgVRdPbrcOgJrVdJ1%2BOFB%2BKmNFp%2BvKXDI7s0iS95bnhTwafynrRWaETIIS4BsqfecyX4OLDg9ctdHEoW2oirS7xwdjEtgkzSIjLML3lHZ9G6CT6E4%2B2nC2tFb16FasfBFeEdHlifbQwon68cnk2yOag9zg8ObxKWjQYM1RtbtWQBKW8pJiTeDUbi%2BOwoqpilrwYyLecGGb5NYKPChZRE%2F2mJEDfPoerBufuXJ4gnltp9VTNcWaAn%2FO6Mlas3xOEH%2FQ%3D%3D&Expires=1710393569
