# 证书下单接口
# https://docs.pki.plus/docs/certificate/certificate-submit

class CertificateCreateRequest(object):
    unique_id = "" # 必传,合作伙伴系统的证书id
    product_id = "" # 必传, /product/list 接口返回的 id
    period = "" # 必传,时长,可选Quarterly,Annually,Biennially
    domain_dcv = {
        # 域名+验证信息，必传，一条域名对应一种验证类型
        # ⚠️注意：通配符只支持dns或email验证
        # ⚠️注意：http、https为子域名文件验证必须上传到子域名本身服务下，不支持传主域名或其他域名
        # ⚠️注意：邮箱验证不支持whois邮箱，只支持admin@、administrator@、postmaster@、webmaster@、hostmaster@ + <子域名 或 主域名> 组合的邮箱
    }
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
