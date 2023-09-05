import boto3
import time

regions = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'ap-northeast-1', 'ap-northeast-2',
           'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-3', 'ca-central-1', 'eu-central-1',
           'eu-west-1', 'eu-west-2', 'ap-south-1', 'eu-west-3', 'eu-north-1', 'sa-east-1']

# Menyimpan data subnet ke dalam file subnet.txt
def save_subnet_data(subnets):
    with open('subnet.txt', 'w') as file:
        for region, subnet_list in subnets.items():
            file.write(f"{region} = {', '.join(subnet_list)}\n")

# Membaca data subnet dari file subnet.txt
def read_subnet_data():
    subnets = {}
    with open('subnet.txt', 'r') as file:
        for line in file:
            region, subnet_data = line.strip().split(' = ')
            subnets[region] = subnet_data.split(', ')
    return subnets

# Menghapus file subnet.txt
def delete_subnet_file():
    import os
    if os.path.exists('subnet.txt'):
        os.remove('subnet.txt')

# Mengambil data subnet dari setiap region dan menyimpannya ke dalam file subnet.txt
def get_subnet_data():
    subnets = {}
    for region in regions:
        ec2_client = boto3.client('ec2', region_name=region)
        response = ec2_client.describe_subnets(Filters=[{'Name': 'default-for-az', 'Values': ['true']}])
        subnet_list = [subnet['SubnetId'] for subnet in response['Subnets']]
        
        if not subnet_list:
            # Buat VPC default di region yang tidak memiliki subnet
            vpc_response = ec2_client.create_default_vpc()
            vpc_id = vpc_response['Vpc']['VpcId']
            
            # Tunggu hingga VPC selesai dibuat
            while True:
                vpc_response = ec2_client.describe_vpcs(VpcIds=[vpc_id])
                state = vpc_response['Vpcs'][0]['State']
                if state == 'available':
                    break
                time.sleep(5)
            
            # Dapatkan subnet baru dari VPC default yang dibuat
            response = ec2_client.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
            subnet_list = [subnet['SubnetId'] for subnet in response['Subnets']]
        
        subnets[region] = subnet_list
    return subnets

# Input dari user
cluster_name = input("Masukkan nama cluster: ")
cpu = input("Masukkan jumlah CPU: ")
memory = input("Masukkan jumlah memori: ")
docker_image = input("Masukkan nama image Docker: ")
desired_count = int(input("Masukkan jumlah tugas (task) yang ingin dibuat: "))

# Mendapatkan data subnet
subnet_data = get_subnet_data()

# Menyimpan data subnet ke dalam file subnet.txt
save_subnet_data(subnet_data)

# Definisi tugas JSON
task_definition = {
    "family": "task-2",
    "networkMode": "awsvpc",
    "containerDefinitions": [
        {
            "name": "fargate-app",
            "image": docker_image,
            "command": []
        }
    ],
    "requiresCompatibilities": [
        "FARGATE"
    ],
    "cpu": str(cpu),
    "memory": str(memory)
}

# Membuat layanan di setiap region dengan menggunakan data subnet
for region, subnet_ids in subnet_data.items():
    # Buat objek klien ECS di region yang diinginkan
    ecs = boto3.client('ecs', region_name=region)
    
    # Buat cluster baru
    response = ecs.create_cluster(clusterName=cluster_name)
    print(f"Cluster {cluster_name} berhasil dibuat di region {region}")
    
    # Buat definisi tugas
    response = ecs.register_task_definition(**task_definition)
    print(f"Definisi tugas berhasil dibuat di region {region}")
    
    # Buat layanan dengan subnet dari file subnet.txt
    if subnet_ids:
        response = ecs.create_service(
            cluster=cluster_name,
            serviceName=f"{cluster_name}-service",
            taskDefinition=task_definition['family'],
            capacityProviderStrategy=[
                {
                    'capacityProvider': 'FARGATE',
                    'weight': 1
                },
                {
                    'capacityProvider': 'FARGATE_SPOT',
                    'weight': 1
                }
            ],
            desiredCount=desired_count,
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': subnet_ids,
                    'assignPublicIp': 'ENABLED'
                }
            }
        )
        print(f"Layanan berhasil dibuat di region {region} dengan subnet {', '.join(subnet_ids)}")
    else:
        print(f"Tidak ada subnet yang tersedia di region {region}")

# Hapus file subnet.txt setelah selesai
delete_subnet_file()

print("DONE!")
