import csv

from urllib3.exceptions import InsecureRequestWarning

import requests ,ssl, json
from requests.auth import HTTPDigestAuth
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


username = 'cdrapi'
password = 'cdrapi1231'
url =  'https://72.137.146.94:8443/cdrapi?format=JSON&caller=1000&numRecords=10'
# 'https://72.137.146.94:8443/recapi'
r = requests.get(url, auth=HTTPDigestAuth(username,password) ,verify=False)
data = json.loads(r.content)
# print(json.loads(r.content))


list =data['cdr_root']
call_history=[]
for item in list:
    call_dict = {}
    if len(item) == 33:

        call_dict['cdr'] = item['cdr']
        call_dict['dst'] = item['dst']
        call_dict['lastdata'] = item['lastdata']
        call_dict['disposition'] = item['disposition']
        call_dict['answer'] = item['answer']
        call_dict['recordfiles'] = item['recordfiles']
        call_dict['end'] = item['end']
        # with open('test.csv', 'w') as f:
        #     for key in call_dict.keys():
        #         f.write("%s,%s\n" % (key, call_dict[key]))

        call_history.append(call_dict)
        print("--------------------------")
    else:
        for key, value in item.items():
            if(key=='cdr'):
                call_dict['cdr'] = item['cdr']

            if (key != 'cdr'):

                    call_dict['dst'] = value['dst']
                    call_dict['lastdata'] = value['lastdata']
                    call_dict['duration'] = value['duration']
                    call_dict['disposition'] = value['disposition']
                    call_dict['answer'] = value['answer']
                    call_dict['recordfiles'] = value['recordfiles']
                    call_dict['end'] = value['end']
                    # with open('test.csv', 'w') as f:
                    #     for key in call_dict.keys():
                    #         f.write("%s,%s\n" % (key, call_dict[key]))
                    call_history.append(call_dict)

                    print("--------------------------")
print(call_history)
print(len(call_history))

# if value['answer'] is None:
# print('NUll Value')
# print("--------------------------")
# call_dict['cdr'] = value['cdr']
# call_dict['dst'] = value['dst']
# call_dict['lastdata'] = value['lastdata']
# call_dict['duration'] = value['duration']
# call_dict['disposition'] = value['disposition']
# call_dict['answer'] = value['answerecordfiles']
# call_dict['end'] = value['end']
# # with open('test.csv', 'w') as f:
# #     for key in call_dict.keys():
# #         f.write("%s,%s\n" % (key, call_dict[key]))
# call_history.append(call_dict)

# else:


# with open('myfile.csv','w') as f:
#     for sublist in call_history:
#         for item in sublist:
#             f.write(item + ',')
#         f.write('\n')
#

# with open('output.csv','wb') as result_file:
#     wr = csv.writer(result_file, dialect='excel')
#     wr.writerow(call_dict)
#
#


# f= open("ubaid.csv","wb")
# f.write(call_history)
# f.close()