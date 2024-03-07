#!/bin/bash

curl -o image.png "https://dynaimage.cdn.cnn.com/cnn/c_fill,g_auto,w_1200,h_675,ar_16:9/https%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F200617130257-01-uva-reworked-logo-0616.jpg"

aws s3 cp image.png s3://ds2002-gwu8ek

presigned_url=$(aws s3 presign --expires-in 604800 s3://ds2002-gwu8ek/image.png)

echo "Presigned URL: $presigned_url"

#https://ds2002-gwu8ek.s3.us-east-1.amazonaws.com/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIATCKAQDQ6QH7VY77M%2F20240305%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240305T221459Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDO%2FdS3%2BuFoj%2FkoFTgiLEAcXQNMNT%2FzXJfGRRRRTlprQDj7lhrP7bCnuCyIVWPMajByUDG%2BmG%2BZzWk6opCK0nPOGvlYt4XyeBgAaPqcbiufbh7XT0zeL7tNUKXdCBXls05vhiLgkW%2F%2BqZsm3pqTXBtiBdiS037pYSZbEviWKjJtMPKqKe2jBvjAvsYt38BQzEXl8ilsLP1OKoM2oj3ZTAApK0kHlNjcrLjbPD5epr%2FDw9zBaGimyG0tCwmaG4bGaxtPcx%2BltSm9%2FJftuCJazKZqiX8%2FAo%2BPedrwYyLSTuKlde2Vn0AVi4jn%2FZuZNRun6kR0EQqpo63eLw2C%2FDij8MRZUw0ICQgLmaZw%3D%3D&X-Amz-Signature=e56cce2f23fac119ddf43badac8c56a4fc3b2350be5460fbf703efe937a57cbf
