# 重签证书请求
class CertificateReissueRequest(object):
    quantum_id = "" # 必传,下单时返回的id
    domain_dcv = {} # 必传
    csr = "" # 必传,客户上传的CSR
    renew = 0 # OV/EV必传,是否为续费订单
    organization = "" # OV/EV必传,公司名称
    organization_unit = "" # OV/EV必传,公司部门
    registered_address_line1 = "" # OV/EV必传,公司注册地址
    serial_no = "" # OV/EV必传,公司注册号，三证合一
    country = "" # OV/EV必传,2位国别码，大写
    state = "" # OV/EV必传,省份
    city = "" # OV/EV必传,城市
    postal_code = "" # OV/EV必传,邮编
    organization_phone = "" # OV/EV必传,组织注册登记电话
    date_of_incorporation = "" # OV/EV必传,成立日期
    contact_name = "" # OV/EV必传,联系人
    contact_title = "" # OV/EV必传,联系人职位
    contact_phone = "" # OV/EV必传,联系人电话
    contact_email = "" # 必传,联系人邮箱
    notify_url = "" # 必传,证书颁发后的通知地址
