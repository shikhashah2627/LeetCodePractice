class Interview:
    def __init__(self):
        self.existing_hosts = [           {
                "type": "viewpoint",
                "nodeId": "05d31a91-93dd-4007-85b1-c2299bfee494",
                "hostname": "10.70.33.80"
            },
            {
                "hostname": "10.70.33.76",
                "status": "operational",
                "nodeId": "3d1e250c-523c-4df7-90ea-4d362e5458a7",
                "instanceId": "i-02625de23fbab5acb",
                "instanceType": "m4.10xlarge",
                "type": "database"
            },
            {
                "hostname": "10.70.33.75",
                "status": "operational",
                "nodeId": "4g1e250c-523c-4df7-90ea-4d362e5458a7",
                "instanceId": "i-02525de23fbab5acb",
                "instanceType": "m4.10xlarge",
                "type": "database"
            }
        ]

        self.new_hosts = [
            {
                "hostname": "10.70.33.76",
                "status": "operational",
                "nodeId": "3d1e250c-523c-4df7-90ea-4d362e5458a7",
                "instanceId": "id",
                "instanceType": "m4.10xlarge11",
                "type": "database"
            },
            {
                "hostname": "10.70.33.275",
                "status": "operational",
                "nodeId": "4g1e250c-523c-4df7-90ea-4d362e545834",
                "instanceId": "i-02525de23fbab5bcd",
                "instanceType": "m4.10xlarge",
                "type": "database"
            },
            {
                "hostname": "10.70.33.176",
                "status": "operational",
                "instanceId": "i-02525de23fbab384d",
                "instanceType": "m4.10xlarge",
                "type": "database"
            }
        ]
        
    """
 
    Problem: Get database nodes from existing hosts list and compare with new database nodes list. If the hostaname of existing host matches with new host, update instanceid and instancetype fields of existing host. 
    Otherwise add 'isDeleted' flag to existing host record. If the new host record is not found in existing list, add it to the existing list.

    """    

    def compare(self):
        # print(self.new_hosts[0]['hostname'])
        hostNameExistingList = []
        indexList = []
        hostNameNewList = []
        for i in range(len(self.existing_hosts)):
            for k, v in self.existing_hosts[i].items():
                if k == 'hostname':
                    hostNameExistingList.append(v)
                    for j in range(len(self.new_hosts)):
                        for k1, v1 in self.new_hosts[j].items():
                            if k1 == 'hostname':
                              hostNameNewList.append(v1)                   
                            if v == v1:
                              self.existing_hosts[i]['instanceId'] = self.new_hosts[j]['instanceId']
                              self.existing_hosts[i]['instanceType'] = self.new_hosts[j]['instanceType']
        
            if self.existing_hosts[i]['hostname'] not in hostNameNewList:
                self.existing_hosts[i]['isDeleted'] = True
                  
        # list of the  hosts which are not in exisiting list                       
        notExisiting = list(set(hostNameNewList) - set(hostNameExistingList))  
        for i in range(len(self.new_hosts)):
            for k, v in self.new_hosts[i].items():
                if k == 'hostname' and v in notExisiting:
                    self.existing_hosts.append(self.new_hosts[i])
        return self.existing_hosts
    
            
            

if __name__ == "__main__":
    interview = Interview()
    print(interview.compare())
       