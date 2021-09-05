import boto3
from balance_recorder.balance_recorder import BalanceRecorderI

s3_client = boto3.client('s3')


class S3BalanceRecorder(BalanceRecorderI):
    def __init__(self, **kwargs):
        self.bucket_name = kwargs.get('bucket', "")
        self.file_name = kwargs.get('file_name', "")

    def save(self, balance_sheet):
        data = str({
                "revenue": balance_sheet.get_revenue(),
                "balance": balance_sheet.get_balance(),
            })
        s3 = boto3.resource("s3")
        s3.Bucket(self.bucket_name)
        s3_client.put_object(
            Key=self.file_name,
            Body=data.encode("utf-8"),
            Bucket=self.bucket_name
        )
