from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging

from poos.lib import get_toml


class TencentCos():
    def __init__(self):
        self.tencent_cos_cfg = get_toml()
        if self.tencent_cos_cfg['tencent-cos']['secret_id'] and self.tencent_cos_cfg['tencent-cos']['secret_key']:
            self.COS_SECRET_ID = self.tencent_cos_cfg['tencent-cos']['secret_id']
            self.COS_SECRET_KEY = self.tencent_cos_cfg['tencent-cos']['secret_key']

    def SearchBucket(self):
        # 正常情况日志级别使用INFO，需要定位时可以修改为DEBUG，此时SDK会打印和服务端的通信信息
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        # 1. 设置用户属性, 包括 secret_id, secret_key, region等。Appid 已在CosConfig中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
        secret_id = self.COS_SECRET_ID  # 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参考https://cloud.tencent.com/document/product/598/37140
        secret_key = self.COS_SECRET_KEY  # 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参考https://cloud.tencent.com/document/product/598/37140
        region = 'ap-beijing'  # 替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
        # COS支持的所有region列表参见https://cloud.tencent.com/document/product/436/6224
        token = None  # 如果使用永久密钥不需要填入token，如果使用临时密钥需要填入，临时密钥生成和使用指引参见https://cloud.tencent.com/document/product/436/14048
        scheme = 'https'  # 指定使用 http/https 协议来访问 COS，默认为 https，可不填

        config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token,
                           Scheme=scheme)
        client = CosS3Client(config)

        response = client.list_buckets()
        # print(response['Buckets'])
        return response
