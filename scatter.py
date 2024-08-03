import matplotlib.pyplot as plt
import numpy as np
import os

# plot1 = fig.add_subplot(1, 2, 1)
# plot2 = fig.add_subplot(1, 2, 2, sharex=plot1, sharey=plot1)


fig, ax = plt.subplots()

final = [] 
final_Txx= []
final_Txy= []
final_Rxx= []
final_Rxy= []

def read_p2m_file(file_path):
    
    with open('paths/'+file_path, 'rb') as file:
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
    # print(x.shape)
    # print(len(final_Rxx),len(final_Rxx),len(final_Rxx))
    
    # plot1.scatter(final_Rxx,final_Rxy)
    # plot2.scatter(final_Txx,final_Txx,color='red')
    
    ax.scatter(final_Rxx, final_Rxy, color='blue', label='Receivers')

    # Plot the second scatter plot
    ax.scatter(final_Txx, final_Txy, color='red', label='Transmitter')

    # Add labels and title
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_title('Transmitter and Receiver Positions')

    # Add a legend
    ax.legend()
    # plt.show()
    fig.savefig('graphs/'+file_path[:-4]+'_graph.png')
    
    
    # np.savez('outputs/path_bld04_tx001_ouput', data = x, comments="Processed data for file \'path_bld04_tx001.p2m\'.\nShape of the numpy array - (29229,45,3,3).\n29229 - Total number of Tx, Rx pairs.\n45 - Paths per Tx Rx pair.\n3 - [Tx,Rx,Req. Data].\n3- Tx - [x,y,z].\n   Rx - [x,y,z].\n   Req. Data - [Power, Delay, No. of Diffractions/Reflections].\n")
    
        
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
        if Tx[0] not in final_Txx and Tx[1] not in final_Txy:
            final_Txx.append(Tx[0])
            final_Txy.append(Tx[1])
    
    
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
    # print(result[0][1])
    
    final_Rxx.append(result[0][1][0])
    final_Rxy.append(result[0][1][1])
    
    return j
      
def find_max(j,pair_paths,data):
    for _ in range(pair_paths):
        line = data[j].decode('utf-8').strip().split()
        j = j+int(line[1]) + 4
    return j    
            
if __name__ == "__main__":
    directory = 'paths'

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    print(files)
    for i in range(1):
        print(files[i])
        file_path = files[i]
    read_p2m_file(file_path)