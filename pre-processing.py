# import struct
# import numpy as np

# final = [] 

# def read_p2m_file(file_path):
    
#     with open(file_path, 'rb') as file:
#         data = file.readlines()
        
        
#         total_entries = int(data[1].decode('utf-8').strip())  
#         pair_paths = int(data[2].decode('utf-8').strip().split()[1])
        
#         max_pairs = pair_paths
        
#         j = 4
#         j = find_max(j,pair_paths,data)
#         for _ in range(total_entries-1):
            
#             pair_paths = int(data[j].decode('utf-8').strip().split()[1])
            
#             if pair_paths > max_pairs:
#                 max_pairs = pair_paths
            
#             if pair_paths == 0:
#                 j = find_max(j + 1,pair_paths,data)
#             else:
#                 j = find_max(j + 2,pair_paths,data)
        
#         pair_paths = int(data[2].decode('utf-8').strip().split()[1])
#         j = 4
#         j = get_data(j,pair_paths,data,max_pairs)
        
#         for i in range(0):
#             pair_paths = int(data[j].decode('utf-8').strip().split()[1])
            
#         #     # if pair_paths == 0:
#         #     #     j = get_data(j + 1,pair_paths,data)
#         #     # else:
#         #     #     j = get_data(j + 2,pair_paths,data)
            

#             j = get_data(j + 2,pair_paths,data,max_pairs)
    
#     x = np.array(final)
#     print(x)    

        
# def get_data(j,pair_paths,data,max_pairs):
#     result = []
#     for i in range(pair_paths):
#         line = data[j].decode('utf-8').strip().split()
        
#         Tx = data[j+2].decode('utf-8').strip().split()
#         Tx = [float(i) for i in Tx]
#         j = j+int(line[1]) + 4
#         power = float(line[2])
#         aoa = float(line[3])
#         diff = int(line[1])
#         Rx = data[j-1].decode('utf-8').strip().split()
            
#         Rx = [float(i) for i in Rx]
#         tmp = [Tx,Rx,[power,aoa,diff]]
#         # print(tmp)    
#         result.append(tmp)
#         # print(result)
    
#     print(len(result))  
    
#     final.append(result)
#     return j
    
#     # np.save('path_bld01_tx001_Output_Pair1.npy', x)
    

# def find_max(j,pair_paths,data):
#     for _ in range(pair_paths):
#         line = data[j].decode('utf-8').strip().split()
#         j = j+int(line[1]) + 4
#     return j    

    
            
# if __name__ == "__main__":
#     file_path = 'path_bld01_tx001.p2m'
#     read_p2m_file(file_path)
    
    
    