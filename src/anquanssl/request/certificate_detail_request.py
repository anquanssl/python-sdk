# 证书查询接口
# https://docs.pki.plus/docs/certificate/certificate-status
class CertificateDetailRequest(object):
    service_id = "" # 证书编号，证书下单接口返回的 `service_id`
    