[<p align="center"><img src="https://github.com/anquanssl/.github/raw/main/profile/logo_dark.png" width="600" height="85"/></p>](https://www.anquanssl.com?__utm_from=github-org-profile#gh-dark-mode-only)
[<p align="center"><img src="https://github.com/anquanssl/.github/raw/main/profile/logo_light.png" width="600" height="85"/></p>](https://www.anquanssl.com?__utm_from=github-org-profile#gh-light-mode-only)

## AnquanSSL

AnquanSSL, aka "Security SSL", also known as "安全 SSL" in Mandarin, founded in 2018, and our mission is providing affordable, secure, and enhanced TLS utilization experiences in the Greater China market.

这是 [安全SSL](https://www.anquanssl.com) 开放API的 Python SDK.

[获取](https://www.anquanssl.com/dashboard/api-credentials) `AccessKey` 秘钥对.

此SDK包仅面向开发者提供支持，若您是分销商，您可能需要:
- [AnquanSSL Module for WHMCS]()
- [AnquanSSL Module for idcSmart]()

如果您要其它编程语言的开发者，您可能需要
- [AnquanSSL PHP SDK](https://github.com/anquanssl/sdk)
- [AnquanSSL Python SDK](https://github.com/anquanssl/python-sdk)
- [AnquanSSL NodeJS SDK](https://github.com/anquanssl/nodejs-sdk)
- [AnquanSSL Golang SDK](https://github.com/anquanssl/golang-sdk)
- [AnquanSSL Java SDK](https://github.com/anquanssl/java-sdk)


## 打包 `.whl`

```bash
pip install build
python -m build
```

## 安装

```bash
pip install anquanssl-***-py3-none-any.whl
pip install requests
```

## 使用

```python
import random
import string
from anquanssl.client import Client
from anquanssl.resource.product import Product
from anquanssl.resource.order import Order
from anquanssl.request.certificate_create_request import CertificateCreateRequest
from anquanssl.request.certificate_detail_request import CertificateDetailRequest
from anquanssl.request.certificate_reissue_request import CertificateReissueRequest
from anquanssl.request.certificate_validate_dcv_request import CertificateValidDCVRequest
from anquanssl.request.certificate_refund_request import CertificateRefundRequest

access_key_id = "***"
access_key_secret = "***"

client = Client(access_key_id, access_key_secret)
product = Product(client)
order = Order(client)

#### 产品列表

resp = product.product_list()
print(resp)
print()

#### 证书下单

req = CertificateCreateRequest()
req.product_id = "comodo-positive-multi-domain"
req.period = "annually"
req.csr = '''-----BEGIN CERTIFICATE REQUEST-----
MIICrzCCAZcCAQAwQTELMAkGA1UEBhMCQ04xDTALBgNVBAgTBHRlc3QxDTALBgNV
BAcTBHRlc3QxFDASBgNVBAMTC2V4YW1wbGUuY29tMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAsTKlxXP0Dslu7Dxwp1ZIWD4Q+NW1/O/Y8QvatmEbzbdc
uG7WnNzizmaRFAvXogxad+fgIjipGsqLiH0aKqUIoVfVVRg4icpzshQK0VuGpXXs
fpU+vVLnM6/a48wN7rnPEXIChqGqedtwYoq2yk4cLOhPoWBge3zkkw66U0OimbyH
R/Hl6IX3uI8/ExzTWsCmvABx3/Urli0zAa/9z2wjOqnwLyGeY1weIUlRCHJTMbnr
R2N5FXNfJyw4ZjE1GJcNabEaQd4W62h4p9CiNvzbvcfdmZVDHO/NuI0SUpEtYrUY
1LIvKmWaUHd1wa45MjBCaGceYRksmxPP3BJ/WudqtwIDAQABoCkwJwYJKoZIhvcN
AQkOMRowGDAWBgNVHREEDzANggtleGFtcGxlLmNvbTANBgkqhkiG9w0BAQsFAAOC
AQEAIlgZv7rgp7e8pkub01G2/jIB6RgfacdLYJANnG3Zw6kNlUjZ0FXQKwtN0VgU
qpvlKgI0wDRoH+TnhHBU1vlOx7BPdqFzOH75YVj5lj4aOH1XDP53n3vr5jk50BIL
7sljvxRDzIuNgKEuxtElCkB1cGq8f7kXiEuI6I28GJ43mhMNfPNdD4oBW+3IaP54
BZDGSAY2l+3fREE1GcHl69POkCyrxhT4Py/sSRV1PIO8PpPcTEMi719Lg0WqNXfx
CDPGdEY9hIivuuCsK6XbJN1GyX5IwaF5oEBqjoPHT3KitNyuhE1dWi8iV36ncNEL
ycdBvjwu/hmmP1oOHQ775dhtFA==
-----END CERTIFICATE REQUEST-----'''
# random string
req.unique_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

req.contact_email = "myemail@example.org"
req.domain_dcv = {
    "example.com": "dns",
    "www.example.com": "http",
    "example.org": "dns",
    "*.example.org": "dns",
}
req.notify_url = "https://partner.exmaple.app/notify"

print("certificate_create requst body:", req.__dict__)
resp = order.certificate_create(req)
print("resp", resp)
print()

certCreateResp = resp


#### 证书查询
req = CertificateDetailRequest()
req.service_id = certCreateResp.service_id
resp = order.certificate_detail(req)
print("Detail resp", resp)
print()


#### 证书重签接口
req = CertificateReissueRequest()
req.service_id = certCreateResp.service_id
req.csr = '''-----BEGIN CERTIFICATE REQUEST-----
MIICszCCAZsCAQAwQzELMAkGA1UEBhMCQ04xDTALBgNVBAgTBHRlc3QxDTALBgNV
BAcTBHRlc3QxFjAUBgNVBAMTDTEuZXhhbXBsZS5jb20wggEiMA0GCSqGSIb3DQEB
AQUAA4IBDwAwggEKAoIBAQCuDTKDQEyTRJwng4cGf6SlZLYO7VrVSqrUYgpfTaPD
ZpHHaBoifrwGraAWiPBSgj2qxesTpFgvZxMDllGYi8dO0kJ/M94iA0kIUSeeOjBC
Ia2mnBwOZoV38T/1Qe3OTmwmB8dq9zGVBF7xFvU1DnbkgbToiAEd+12f1CENtnTM
KuAP+prRylqZhqcOjmt4m0inVGI60dvIvpfS0pp9HEdcxEIKaDKt8tFhKcGC3jk6
4z+MmMNMifuMpvNDj/iG1gYH2If4uKNZBENXRshrn21VdYj7kxK4gQfW+qpqfarZ
AurJj9Ms+EMUL4lpTZA100l24BvJnvIXMABjJA0fucjfAgMBAAGgKzApBgkqhkiG
9w0BCQ4xHDAaMBgGA1UdEQQRMA+CDTEuZXhhbXBsZS5jb20wDQYJKoZIhvcNAQEL
BQADggEBAImFUqPAgz4WtF985pIuujGhXqFTu2vSOcCTXpo+ghgKd+h4EB23Vi94
0KqLimSXo6D5iJCdlZP0vo7HAD2v1nds7EkS8bTbrkxmBTGoGL2JfHvI6tGqUyZv
HQjYECUr+GuTKG3erh2u1SRg59HR5x88+/7OvfukaikIs+D0spQPtOnFxahE/qp/
ugERGcF7guZZqMfylMM8U/oVJXeTcjBQAA14nS/XBr8Aed5fdbM9cLdQcqc+DbYC
yXTtEG5GjFBsg0zrPX/p2pBkC8TZPzNTdz5gjQ+A5qJM+eUPhBOlwD/hv5J4pMXo
G0B6+BJV/Ccnd0FNN1GsLtzH33reKZg=
-----END CERTIFICATE REQUEST-----'''
req.unique_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
req.domain_dcv = {
    "1.example.com": "dns",
    "www.1.example.com": "http",
    "2.example.org": "dns",
    "*.2.example.org": "dns",
}
resp = order.certificate_reissue(req)
print("Reissue resp", resp)
print()


#### 检查DCV接口
req = CertificateValidDCVRequest()
req.service_id = certCreateResp.service_id
resp = order.certificate_validate_dcv(req)
print("ValidDCV", resp)
print()


#### 证书退款
req = CertificateRefundRequest()
req.service_id = certCreateResp.service_id
resp = order.certificate_refund(req)
print("Refund", resp)
print()
```

## 贡献

特别鸣谢以下工程师对本项目的贡献:

[@jellnicy](https://github.com/jellnicy)
