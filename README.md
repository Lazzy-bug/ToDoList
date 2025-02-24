# ToDoList Application

This project is a simple ToDoList application.

## Service Configuration

The service configuration is defined in `service.yaml`:

```yaml
# ...existing code...
```

## Deployment

To deploy the application, use the following command:

```sh
kubectl apply -f service.yaml
```

## Usage

Once deployed, the application will be accessible on the specified NodePort.

## Commands

Here are some useful commands for managing the application:

- To get the status of the pods:
  ```sh
  kubectl get pods
  ```

- To describe a specific pod:
  ```sh
  kubectl describe pod <pod-name>
  ```

- To view the logs of a pod:
  ```sh
  kubectl logs <pod-name>
  ```

- To delete a pod:
  ```sh
  kubectl delete pod <pod-name>
  ```

## Docker Commands

- To build the Docker image:
  ```sh
  docker build -t todo-app .
  ```

- To run the Docker container:
  ```sh
  docker run -p 5000:5000 todo-app
  ```

## Minikube Commands

- To start Minikube:
  ```sh
  minikube start
  ```

- To get cluster information:
  ```sh
  kubectl cluster-info
  ```

- To apply the deployment configuration:
  ```sh
  kubectl apply -f deployment.yaml
  ```

- To apply the service configuration:
  ```sh
  kubectl apply -f service.yaml
  ```

- To load the Docker image into Minikube:
  ```sh
  minikube image load todo-app
  ```

- To access the service via Minikube:
  ```sh
  minikube service todo-app-service
  ```

## License

This project is licensed under the MIT License.
