# myportal
Small web app to demonstrate developer workflow

## Workflow description
- Developer uses ServiceNow to order a new Kubernetes "namespace" in the cloud of choice
- Development process starts
- Developer finishes code and runs unit testing (tests to be added in future)
- New code is committed to GitLab (GitLab runs on a VM in the lab)
- GitLab triggers a pipeline in Jenkins (Jenkins runs on a VM in the lab)
- Jenkins tests the code and builds a container image
- The container image is pushed to a repo in DockerHub (https://hub.docker.com/r/cermegno/myportal/tags)
- Developer deploys the container in Kubernetes (sample manifests in the k8s-manifests folder)
- Web app can be accessed as a NodePort on port 30001, ex: http://172.24.164.67:30001/

![Developer Workflow](/dev-workflow.png)

## Demo instructions
- Provision namespace from ServiceNow
- Putty into kube client VM
- Show and describe namespace
- Apply deployment and services manifest
- Show MyPortal app
- Provision S3 bucket
