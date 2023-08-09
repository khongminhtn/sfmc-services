import requests


class Folder:
    def __init__(self):
        pass
    
    def create(self, name, soap_uri, access_token):
        uri = soap_uri + 'Service.asmx'
        headers = {
            'Content-Type': 'text/xml; charset=utf-8'
        }
        payload = f'''
            <?xml version="1.0" encoding="UTF-8"?>
            <s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://schemas.xmlsoap.org/ws/2004/08/addressing"
                xmlns:u="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">

                <s:Header>
                    <a:Action s:mustUnderstand="1">Create</a:Action>
                    <a:To s:mustUnderstand="1">{uri}</a:To>
                    <fueloauth>{access_token}</fueloauth>
                </s:Header>

                <s:Body xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
                    <CreateRequest xmlns="http://exacttarget.com/wsdl/partnerAPI">
                        <Objects xsi:type="DataFolder">
                            <CustomerKey>RANDOM</CustomerKey>
                            <ParentFolder>
                                <ID>48517</ID>
                            </ParentFolder>
                            <Name>{name}</Name>
                            <ContentType>dataextension</ContentType>
                            <IsActive>true</IsActive>
                            <IsEditable>true</IsEditable>
                            <AllowChildren>true</AllowChildren>
                        </Objects>
                    </CreateRequest>
                </s:Body>
            </s:Envelope>
        '''
        response = requests.post(uri, headers=headers, data=payload)
        return response 