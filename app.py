from azure.storage.blob import BlobServiceClient

connection_string = "DefaultEndpointsProtocol=https;AccountName=nook1212;AccountKey=uhqpVxTTXzVw6AwU2EIjSEswFbQWOsytg/4LfBRtjRJNQG5DmQ/xt5BbUXPOgK7akuOQfEkLwTle+ASt9bfwGA==;EndpointSuffix=core.windows.net"
container_name = "data"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

blobs = container_client.list_blobs()
for blob in blobs:
    print(blob.name)
