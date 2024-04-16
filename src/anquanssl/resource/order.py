from ..request.certificate_create_request import CertificateCreateRequest
from ..request.certificate_detail_request import CertificateDetailRequest
from ..request.certificate_reissue_request import CertificateReissueRequest
from ..request.certificate_validate_dcv_request import CertificateValidDCVRequest
from ..request.certificate_refund_request import CertificateRefundRequest

from .abstract_resource import AbstractResource


class Order(AbstractResource):

    def certificate_create(self, certificate_create_request: CertificateCreateRequest):
        return self.client.post('/certificate/create', {}, certificate_create_request.__dict__)

    def certificate_detail(self, certificate_detail_request: CertificateDetailRequest):
        return self.client.get("/certificate/detail", certificate_detail_request.__dict__, {})

    def certificate_reissue(self, certificate_reissue_request: CertificateReissueRequest):
        return self.client.post("/certificate/reissue", {}, certificate_reissue_request.__dict__)

    def certificate_validate_dcv(self, certificate_valid_dcv_request: CertificateValidDCVRequest):
        return self.client.post("/certificate/validate-dcv", {}, certificate_valid_dcv_request.__dict__)
    
    def certificate_refund(self, certificate_refund_request: CertificateRefundRequest):
        return self.client.post("/certificate/refund", {}, certificate_refund_request.__dict__)