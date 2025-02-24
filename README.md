# ToDoList Application

This project is a simple ToDoList application built using Docker and Kubernetes. It provides an easy-to-use interface for managing tasks and demonstrates containerization and orchestration best practices.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Deployment](#deployment)
- [Commands](#commands)
- [Service Configuration](#service-configuration)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Git**: To clone the repository.
- **Docker**: To build and run the application in a containerized environment.
- **Minikube**: To run Kubernetes locally.
- **kubectl**: To interact with the Kubernetes cluster.

### Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Lazzy-bug/ToDoList.git
    cd ToDoList
    ```

2. **Build the Docker Image**:
    ```sh
    docker build -t todo-app .
    ```

3. **Run the Docker Container Locally (Optional)**:
    ```sh
    docker run -p 5000:5000 todo-app
    ```

4. **Start Minikube**:
    ```sh
    minikube start
    ```

5. **Apply the Deployment Configuration**:
    ```sh
    kubectl apply -f deployment.yaml
    ```

6. **Apply the Service Configuration**:
    ```sh
    kubectl apply -f service.yaml
    ```

7. **Load the Docker Image into Minikube**:
    ```sh
    minikube image load todo-app
    ```

8. **Access the Service via Minikube**:
    ```sh
    minikube service todo-app-service
    ```

## Deployment

To deploy the application to a Kubernetes cluster, use the following commands:

```sh
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

The application will be deployed as a Kubernetes pod and exposed via a service.

## Commands

Here are some useful commands for managing the application:

- **Check Deployment Status**:
  ```sh
  kubectl get deployments
  ```

- **Check Pod Status**:
  ```sh
  kubectl get pods
  ```

- **Check Service Status**:
  ```sh
  kubectl get svc
  ```

- **Describe a Specific Pod**:
  ```sh
  kubectl describe pod <pod-name>
  ```

- **View Logs of a Pod**:
  ```sh
  kubectl logs <pod-name>
  ```

- **Delete a Pod**:
  ```sh
  kubectl delete pod <pod-name>
  ```

## Service Configuration

The service configuration is defined in `service.yaml`. Below is an example of what it might look like:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: todo-app-service
spec:
  type: NodePort
  selector:
    app: todo-app
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
```

This configuration exposes the application on port 5000 and maps it to a NodePort for external access.

## Contributing

We welcome contributions! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m "Add YourFeatureName"`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
