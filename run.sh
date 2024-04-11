RG=dc-sb-test
NAME=dc-sb-test
LOCATION=westus3
QUEUE=running

az group create --name ${RG} --location ${LOCATION}

az servicebus namespace create \
	--resource-group ${RG} \
  --name ${NAME} \
  --location ${LOCATION} | tee service-bus.log

az servicebus namespace authorization-rule keys list \
	--name RootManageSharedAccessKey \
  --namespace-name ${NAME}  \
  --resource-group ${RG} \
  --query primaryConnectionString \
  --output tsv   | tee authorized.log

az servicebus queue create \
	--name ${QUEUE} \
	--namespace-name ${NAME} \
	--resource-group ${RG}

