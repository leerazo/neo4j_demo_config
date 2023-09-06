export VM_INSTANCE_NAME='leerazo-neo4j-gcp-genai-demo'
#export VM_INSTANCE_NAME=vm_instance_name
export GCP_PROJECT_NAME=$(gcloud config get-value project)
gcloud compute instances create $VM_INSTANCE_NAME \
    --project=$GCP_PROJECT_NAME \
    --zone=us-central1-c \
    --machine-type=e2-medium \
    --network-interface=network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=default \
    --maintenance-policy=MIGRATE --provisioning-model=STANDARD \
    --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append \
    --tags=allow-http,http-server \
    --create-disk=auto-delete=yes,boot=yes,device-name=$VM_INSTANCE_NAME,image=projects/debian-cloud/global/images/debian-11-bullseye-v20230509,mode=rw,size=10,type=projects/$GCP_PROJECT_NAME/zones/us-central1-c/diskTypes/pd-balanced \
    --no-shielded-secure-boot \
    --shielded-vtpm --shielded-integrity-monitoring \
    --labels=goog-ec-src=vm_add-gcloud --reservation-affinity=any
