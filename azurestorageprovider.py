"""Provides a way to upload video content to Azure Storage."""

from azure.storage.blob import BlockBlobService, ContentSettings

class AzureStorageProvider(object):
    """Class that facilitates connection to Azure Storage."""

    def upload_video(self, account_name='', account_key='', container='', blob='', path=''):
        """Upload video to the provided account."""

        block_blob_service = None

        if account_name and account_key and container and blob:
            block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)
            containers = block_blob_service.list_containers()

            if container not in containers:
                block_blob_service.create_container(container)
        else:
            print 'ERROR: No account credentials for Azure Storage specified.'

        block_blob_service.create_blob_from_path(
            container,
            blob,
            path,
            content_settings=ContentSettings(content_type='video/mp4')
        )
