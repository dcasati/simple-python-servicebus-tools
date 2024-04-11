#  Azure Service Bus simple tools in Python
 
## Prerequisites  
  
Make sure you have the Azure CLI installed on your machine. If not, you can download it from [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).  
  
## Steps to Execute  
  
1. Set your environment variables in your terminal:  
  
```bash  
RG=dc-sb-test  
NAME=dc-sb-test  
LOCATION=westus3  
QUEUE=running  
```  
  
2. Create a resource group in Azure:  
  
```bash  
az group create --name ${RG} --location ${LOCATION}  
```  
  
3. Create a Service Bus namespace and log the output:  
  
```bash  
az servicebus namespace create --resource-group ${RG} --name ${NAME} --location ${LOCATION} | tee service-bus.log  
```  
  
4. Retrieve the connection string for the Service Bus namespace and log the output:  
  
```bash  
az servicebus namespace authorization-rule keys list --name RootManageSharedAccessKey --namespace-name ${NAME} --resource-group ${RG} --query primaryConnectionString --output tsv | tee authorized.log  
```
  
5. Create a queue in the Service Bus namespace:  
  
```bash  
az servicebus queue create --name ${QUEUE} --namespace-name ${NAME} --resource-group ${RG}  
```
  
## Using Python Service Bus Tools  
  
You can use Python tools to send and receive messages from the Service Bus queue. Here are the usage instructions for the `receiver.py` and `sender.py` scripts in the `simple-python-servicebus-tools` directory.  
  
For `receiver.py`:  
  
```bash  
~/src/simple-python-servicebus-tools ./receiver.py
usage: receiver.py [-h] --queue QUEUE [--remove]  
receiver.py: error: the following arguments are required: --queue  
```
  
For `sender.py`:  
  
```bash
~/src/simple-python-servicebus-tools ./sender.py  
usage: sender.py [-h] --queue QUEUE --file FILE  
sender.py: error: the following arguments are required: --queue, --file  
```
There is a sample `job.json` file that can be used as an input payload to a queue
  
Make sure to replace the placeholders with your actual values when running these commands.  
