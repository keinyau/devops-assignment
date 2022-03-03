# Build image 
docker build -t assignment . 

# Docker run application 
docker run -d -p 8000:5000 assignment 

# Get Output 
curl http://localhost:8000

output:
```
Marina Gardens Drive,16:34,0mm,Not Raining
```

# Create Pod 
kubectl apply -f pod.yaml 

# Verify pod 
kubectl get pods -n default | grep rain-app

# Create configmap 
kubectl apply -f config.yaml 

# Create deployment 
kubectl apply -f deploy.yaml 

# Create service 
kubectl apply -f svc.yaml 

# curl service endpoint 
kubectl run -i --tty --rm debug --image=nginx --restart=Never -- sh
```
# curl rain-app-service:8080
Marina Gardens Drive,16:34,0mm,Not Raining
```