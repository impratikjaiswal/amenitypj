from flask import render_template, request
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil
from qr_play.main.data_type.data_type_master import DataTypeMaster
from qr_play.main.helper.constants_config import ConfigConst
from qr_play.main.helper.defaults import Defaults
from qr_play.main.helper.formats import Formats

small_data = 'Welcome To QrPlay'

bulk_data_1 = """}**************************************************{ ToDO
}+++++++++++++++++++++++++{ Explore 
CLI
Cloudshell;  CLI Browser
SDK
ENI is available automatically?
Instance with Custom EBS volume only (EBS snapshot)
}----------------------------------------------------------------------------------------------------{ 
AWS Global Infrastructure
- AWS Regions (e.g. ap-southeast-2 => asia specific Sydney )
- AWS Availability Zones (e.g. ap-southeast-2a, ap-southeast-2b, ap-southeast-2c)
- AWS Data Centers
- AWS Edge Locations /Points of Presence
}----------------------------------------------------------------------------------------------------{ 
Many services are Region-scoped, but few are global (like IAM, Route53)
}----------------------------------------------------------------------------------------------------{ 
Each AZ: one ore more discreate Data centers with redundant power, networking , connectivity. isolated from disasters.
}**************************************************{ IAM: Global Service 
Least Privilege Principle
    Don't give more permission than a user need
One user can be part of multiple groups
Inline IAM Policy (Direct to individual)
    VS 
IAM Policy inheritance (inherit from group)
}**************************************************{ Access AWS
    AWS Management Console  (Access: Password & MFA)
    AWS CLI                 (Access: Access Keys (Access Key ID, Secret Access Key))
    AWS SDK                 (Access: Access Keys)
}**************************************************{     
IAM User    (Permission to user to perform action)
    Vs 
IAM Role    (Permission to service to perform action on your behalf)
}**************************************************{ IAM Security Tools
IAM Credential Report (Account Level)
IAM Access Advisor (User level)
    All service permissions granted and last accessed. helpful to revise policies
}----------------------------------------------------------------------------------------------------{ AWS Billing
Billing Information has to be enabled for IAM Access (if needed)
Bills page has option for "charges by Service"; region specific data is available.
Free tier usage balance
}**************************************************{ Budget
Email Triggers: Actual 85% & 100% or forecast is 100%
}----------------------------------------------------------------------------------------------------{ EC2
If a instance is stopped, AWS is not going to bill it. 
If a instance is stopped & Started, Public IP may changed. Private is fixed.
SSH is not allowed with Private IP unless VPN is not established.
}**************************************************{ SG: Security Group
allow rules; control how traffic is allowed in & out of EC2 instance
can be refence by IP of other SG
if application is not accessible (time out error), then its a SG issue.
if There's a connection refused; This means the instance is reachable, Not an SG issue; its application g"""

bulk_data_2 = """}**************************************************{ ToDO
}+++++++++++++++++++++++++{ Explore 
CLI
Cloudshell;  CLI Browser
SDK
ENI is available automatically?
Instance with Custom EBS volume only (EBS snapshot)
}----------------------------------------------------------------------------------------------------{ 
AWS Global Infrastructure
- AWS Regions (e.g. ap-southeast-2 => asia specific Sydney )
- AWS Availability Zones (e.g. ap-southeast-2a, ap-southeast-2b, ap-southeast-2c)
- AWS Data Centers
- AWS Edge Locations /Points of Presence
}----------------------------------------------------------------------------------------------------{ 
Many services are Region-scoped, but few are global (like IAM, Route53)
}----------------------------------------------------------------------------------------------------{ 
Each AZ: one ore more discreate Data centers with redundant power, networking , connectivity. isolated from disasters.
}**************************************************{ IAM: Global Service 
Least Privilege Principle
    Don't give more permission than a user need
One user can be part of multiple groups
Inline IAM Policy (Direct to individual)
    VS 
IAM Policy inheritance (inherit from group)
}**************************************************{ Access AWS
    AWS Management Console  (Access: Password & MFA)
    AWS CLI                 (Access: Access Keys (Access Key ID, Secret Access Key))
    AWS SDK                 (Access: Access Keys)
}**************************************************{     
IAM User    (Permission to user to perform action)
    Vs 
IAM Role    (Permission to service to perform action on your behalf)
}**************************************************{ IAM Security Tools
IAM Credential Report (Account Level)
IAM Access Advisor (User level)
    All service permissions granted and last accessed. helpful to revise policies
}----------------------------------------------------------------------------------------------------{ AWS Billing
Billing Information has to be enabled for IAM Access (if needed)
Bills page has option for "charges by Service"; region specific data is available.
Free tier usage balance
}**************************************************{ Budget
Email Triggers: Actual 85% & 100% or forecast is 100%
}----------------------------------------------------------------------------------------------------{ EC2
If a instance is stopped, AWS is not going to bill it. 
If a instance is stopped & Started, Public IP may changed. Private is fixed.
SSH is not allowed with Private IP unless VPN is not established.
}**************************************************{ SG: Security Group
allow rules; control how traffic is allowed in & out of EC2 instance
can be refence by IP of other SG
if application is not accessible (time out error), then its a SG issue.
if There's a connection refused; This means the instance is reachable, Not an SG issue; its application g}**************************************************{ ToDO
}+++++++++++++++++++++++++{ Explore 
CLI
Cloudshell;  CLI Browser
SDK
ENI is available automatically?
Instance with Custom EBS volume only (EBS snapshot)
}----------------------------------------------------------------------------------------------------{ 
AWS Global Infrastructure
- AWS Regions (e.g. ap-southeast-2 => asia specific Sydney )
- AWS Availability Zones (e.g. ap-southeast-2a, ap-southeast-2b, ap-southeast-2c)
- AWS Data Centers
- AWS Edge Locations /Points of Presence
}----------------------------------------------------------------------------------------------------{ 
Many services are Region-scoped, but few are global (like IAM, Route53)
}----------------------------------------------------------------------------------------------------{ 
Each AZ: one ore more discreate Data centers with redundant power, networking , connectivity. isolated from disasters.
}**************************************************{ IAM: Global Service 
Least Privilege Principle
    Don't give more permission than a user need
One user can be part of multiple groups
Inline IAM Policy (Direct to individual)
    VS 
IAM Policy inheritance (inherit from group)
}**************************************************{ Access AWS
    AWS Management Console  (Access: Password & MFA)
    AWS CLI                 (Access: Access Keys (Access Key ID, Secret Access Key))
    AWS SDK                 (Access: Access Keys)
}**************************************************{     
IAM User    (Permission to user to perform action)
    Vs 
IAM Role    (Permission to service to perform action on your behalf)
}**************************************************{ IAM Security Tools
IAM Credential Report (Account Level)
IAM Access Advisor (User level)
    All service permissions granted and last accessed. helpful to revise policies
}----------------------------------------------------------------------------------------------------{ AWS Billing
Billing Information has to be enabled for IAM Access (if needed)
Bills page has option for "charges by Service"; region specific data is available.
Free tier usage balance
}**************************************************{ Budget
Email Triggers: Actual 85% & 100% or forecast is 100%
}----------------------------------------------------------------------------------------------------{ EC2
If a instance is stopped, AWS is not going to bill it. 
If a instance is stopped & Started, Public IP may changed. Private is fixed.
SSH is not allowed with Private IP unless VPN is not established.
}**************************************************{ SG: Security Group
allow rules; control how traffic is allowed in & out of EC2 instance
can be refence by IP of other SG
if application is not accessible (time out error), then its a SG issue.
if There's a connection refused; This means the instance is reachable, Not an SG issue; its application issue in instance
}**************************************************{ 
IA: Infrequent Access
"""


def get_sample_data(key):
    sample_data = {
        'sample_1': {
            'remarks_list': 'Simple Qr',
            'raw_data': small_data,
            'scale': 8,
            'split_qrs': False
        },
        'sample_2': {
            'remarks_list': 'Bulk Data Single Qr',
            'raw_data': bulk_data_1,
            'scale': 5,
            'split_qrs': False,
        },
        'sample_3': {
            'remarks_list': 'Bulk Data Split Qrs',
            'raw_data': bulk_data_2,
            'scale': 5,
            'split_qrs': True,
        },
    }
    return sample_data.get(key, None)


def handle_requests():
    """

    :return:
    """

    page_url = 'qrPlay.html'
    default_data = {
        'version': f'v{ConfigConst.TOOL_VERSION}',
        'sample_processing': 'load_only',
        'qr_code_versions': range(40, 0, -1),
        'selected_qr_code_version': Defaults.QR_CODE_VERSION,
        'split_qrs': Defaults.SPLIT_QRS,
        # 'scale': Defaults.SCALE,
        'scale': 5,
        'output_data': '',
    }
    if request.method == 'GET':
        return render_template(page_url, **default_data)
    if request.method == 'POST':
        PhUtil.print_iter(request.form, header='request.form')
        sample_processing = request.form['sample_processing']
        # if not request.form['raw_data']:
        #     flash('raw_data is required!')
        sample_data_dict = None
        for key in request.form.keys():
            if not key.startswith('sample'):
                continue
            sample_data_dict = get_sample_data(key)
            if sample_data_dict:
                break
        if sample_data_dict and sample_processing == 'load_only':
            # Data Processing is not needed
            pass
        else:
            # Data Processing is needed in all other cases
            # Filter All Sample Keys
            dic_to_process = {k: v for k, v in
                              (sample_data_dict if sample_data_dict else request.form.to_dict()).items() if
                              not k.startswith('sample')}
            dic_to_process.update({'image_format': Formats.PNG_URI})
            data_type = DataTypeMaster()
            data_type.set_data_pool(data_pool=dic_to_process)
            data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
            temp_output_data = []
            output_data = data_type.get_output_data()
            if isinstance(output_data, list):
                temp_output_data = output_data
            else:
                temp_output_data.append(output_data)
            default_data.update({'output_data': temp_output_data})
        if sample_data_dict:
            default_data.update({'raw_data': sample_data_dict.get('raw_data')})
            if 'split_qrs' in sample_data_dict:
                default_data.update({'split_qrs': sample_data_dict.get('split_qrs')})
            if 'qr_code_version' in sample_data_dict:
                default_data.update({'qr_code_version': sample_data_dict.get('qr_code_version')})
            if 'scale' in sample_data_dict:
                default_data.update({'scale': sample_data_dict.get('scale')})
            default_data.update({'remarks_list': sample_data_dict.get('remarks_list')})
        else:
            default_data.update({'raw_data': request.form['raw_data']})
            default_data.update({'split_qrs': True if 'split_qrs' in request.form.keys() else False})
            default_data.update({'qr_code_version': request.form['qr_code_version']})
            default_data.update({'scale': request.form['scale']})
            default_data.update({'remarks_list': request.form['remarks_list']})
        default_data.update({'sample_processing': sample_processing})
        return render_template(page_url, **default_data)
    return render_template(page_url, **default_data)
