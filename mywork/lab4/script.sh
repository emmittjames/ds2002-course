#!/bin/bash

curl -o image.png "https://dynaimage.cdn.cnn.com/cnn/c_fill,g_auto,w_1200,h_675,ar_16:9/https%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F200617130257-01-uva-reworked-logo-0616.jpg"

aws s3 cp image.png s3://ds2002-gwu8ek

presigned_url=$(aws s3 presign --expires-in 604800 s3://ds2002-gwu8ek/image.png)

echo "Presigned URL: $presigned_url"

#https://ds2002-gwu8ek.s3.us-east-1.amazonaws.com/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIATCKAQDQ6VJAWGMPC%2F20240307%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240307T052446Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDKZfIhYo%2Bo6apTgghyLEAbRd0zOZRZCz8NFGTp8FJJuI%2BjAoD9%2BgUrrbOZ6UG6BvMHcyjzFCZZNu%2B3NoqTiayEwWjhxXlvSMLgVRdPbrcOgJrVdJ1%2BOFB%2BKmNFp%2BvKXDI7s0iS95bnhTwafynrRWaETIIS4BsqfecyX4OLDg9ctdHEoW2oirS7xwdjEtgkzSIjLML3lHZ9G6CT6E4%2B2nC2tFb16FasfBFeEdHlifbQwon68cnk2yOag9zg8ObxKWjQYM1RtbtWQBKW8pJiTeDUbi%2BOwoqpilrwYyLecGGb5NYKPChZRE%2F2mJEDfPoerBufuXJ4gnltp9VTNcWaAn%2FO6Mlas3xOEH%2FQ%3D%3D&X-Amz-Signature=5770824f348ab14778d54be5d0800ef6257f3425e0918772d70eb235df38914d
