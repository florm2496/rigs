#pip install gputil
#pip install tabulate
import GPUtil
from tabulate import tabulate


def get_gpus():
    print("="*40, "GPU Details", "="*40)
    gpus = GPUtil.getGPUs()
    list_gpus = []
    gpus_json=[]
    for gpu in gpus:
        gpu_j={}
        # get the GPU id
        gpu_id = gpu.id
        # name of GPU
        gpu_name = gpu.name
        # get % percentage of GPU usage of that GPU
        gpu_load = f"{gpu.load*100}%"
        # get free memory in MB format
        gpu_free_memory = f"{gpu.memoryFree}MB"
        # get used memory
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        # get total memory
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        # get GPU temperature in Celsius
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        
        gpu_j['gpu_id']=gpu_id
        gpu_j['gpu_free_memory']=gpu_free_memory
        gpu_j['gpu_load']=gpu_load
        gpu_j['gpu_used_memory']=gpu_used_memory
        gpu_j['gpu_temperature']=gpu_temperature
        gpu_j['gpu_uuid']=gpu_uuid
        
        gpus_json.append(gpu_j)
        
        
        list_gpus.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
            gpu_total_memory, gpu_temperature, gpu_uuid
        ))
    print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory", "temperature", "uuid")))
    return gpus_json


# #uid
# uid: uid,
#           propietario: propietario,
#           userNameBingBon: userNameBingBon,
#           passwordBingBon: passwordBingBon,