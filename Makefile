ROJECT_ID:=bank-306009
SERVICE_NAME:=daimler
IMAGE:=gcr.io/${ROJECT_ID}/${SERVICE_NAME}
REGION:=europe-north1

build:
	docker image build -t ${IMAGE} .

local:
	docker container run -p 8080:8080 ${IMAGE}
