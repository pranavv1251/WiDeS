import numpy as np

final = [] 

def read_p2m_file(file_path):
    
    with open(file_path, 'rb') as file:
        data = file.readlines()
        
        
        total_pairs = int(data[1].decode('utf-8').strip())  
        pair_paths = int(data[2].decode('utf-8').strip().split()[1])
        
        max_pairs = pair_paths
        
        j = 4
        j = find_max(j,pair_paths,data)
        
        for _ in range(total_pairs - 1):
            
            pair_paths = int(data[j].decode('utf-8').strip().split()[1])
            
            if pair_paths > max_pairs:
                max_pairs = pair_paths
            
            if pair_paths == 0:
                j = find_max(j + 1,pair_paths,data)
            else:
                j = find_max(j + 2,pair_paths,data)
        
        pair_paths = int(data[2].decode('utf-8').strip().split()[1])
        j = 4
        j = get_data(j,pair_paths,data,max_pairs)
        
        for i in range(total_pairs - 1):
            pair_paths = int(data[j].decode('utf-8').strip().split()[1])
            
            if pair_paths == 0:
                j = get_data(j + 1,pair_paths,data,max_pairs)
            else:
                j = get_data(j + 2,pair_paths,data,max_pairs)
            
    x = np.array(final)   
    print(x.shape)
    np.savez('outputs/path_bld09_tx003_ouput', data = x, comments="Processed data for file \'path_bld09_tx003.p2m\'.\nShape of the numpy array - (29229,45,3,3).\n29229 - Total number of Tx, Rx pairs.\n45 - Paths per Tx Rx pair.\n3 - [Tx,Rx,Req. Data].\n3- Tx - [x,y,z].\n   Rx - [x,y,z].\n   Req. Data - [Power, Delay, No. of Diffractions/Reflections].\n")
    
        
def get_data(j,pair_paths,data,max_pairs):
    result = []
    for i in range(pair_paths):
        line = data[j].decode('utf-8').strip().split()
        
        Tx = data[j+2].decode('utf-8').strip().split()
        Tx = [float(i) for i in Tx]
        j = j+int(line[1]) + 4
        power = float(line[2])
        aoa = float(line[3])
        diff = int(line[1])
        Rx = data[j-1].decode('utf-8').strip().split()
            
        Rx = [float(i) for i in Rx]
        tmp = [Tx,Rx,[power,aoa,diff]]
        result.append(tmp)
    
    # print(len(result))  
    
    if len(result) < max_pairs:
        if pair_paths == 0:
            for _ in range(max_pairs):
                tmp = [[float('Nan'),float('Nan'),float('Nan')],[float('Nan'),float('Nan'),float('Nan')],[float('Nan'),float('Nan'),float('Nan')]]
                result.append(tmp)
        else:        
            for _ in range(len(result), max_pairs):
                tmp = [Tx,Rx,[float('Nan'),float('Nan'),float('Nan')]]
                result.append(tmp)
    final.append(result)
    return j
      
def find_max(j,pair_paths,data):
    for _ in range(pair_paths):
        line = data[j].decode('utf-8').strip().split()
        j = j+int(line[1]) + 4
    return j    
            
if __name__ == "__main__":
    file_path = 'path_bld09_tx003.p2m'
    read_p2m_file(file_path)