import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():

          print ('Bucket: ' + bucket.name)
          s3x = boto3.client('s3')
         
          try:
              bucket_tagging = s3x.get_bucket_tagging(Bucket=bucket.name)
              tag_set = bucket_tagging['TagSet']
              for tag in tag_set:
                  print(tag)
          except:
              print("NO TAGS")
              print("------------------------------------------------------------------")
          else:
              print("------------------------------------------------------------------")












# Create an S3 client
#s3 = boto3.client('s3')

# Call S3 to get bucket tagging
#bucket_tagging = s3.get_bucket_tagging(Bucket='my-bucket')

# Get a list of all tags
#tag_set = bucket_tagging['TagSet']

# Print out each tag
#for tag in tag_set:    
#        print(tag)                

