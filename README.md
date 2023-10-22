# Technical Test: Microservice Project

## Description

This document will outline the requirements, tools, and technologies I utilized to meet the requested criteria.

The reproduction of this project should only be for evaluation and feedback purposes.

## Whoami

I am a sysadmin with over:

- 3 years administering Kubernetes.
- 5 years in Docker administration.
- 5 years of advanced GIT knowledge.
- 20 years of advanced GNU/Linux administration.
- Proficient in: 3 years with Python, 1 year with Java, Go, Ruby, and Node.
- 5 years knowledgeable in CI/CD pipelines, on both local platforms and in the cloud.
- 7 years in Cloud Computing management with Microsoft Azure, AWS, Google Cloud Platform, OCI.
- 5 years of experience in IaC (Infrastructure as Code), with traditional providers, as well as OCI, VMware, and Digital Ocean.

## Schema

Constructed based on technology, services, and goals is a directory tree, which contains the current repository project.

![schema][schema]

## Requirements

You should install the following tools on your local machine:

- ngrok.
- Python.
- Docker Desktop.

A microservice is constructed containing a REST EndPoint called: `/DevOps`.

- We use Python as the programming language and Flask as the Framework.
- A script from the project is used to generate a token, in case the current JWT has expired:

```bash
python docker/python/Scripting/generate_jwt.py
```

- We use the HTTP POST method on the JSON file to utilize the Payload with the required API Key, validating all request fields:

```bash
curl -X POST \
-H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" \
-H "X-JWT-KEY: $JWT_Token" \
-H "Content-Type: application/json" \
-d '{"message": "This is a test", "to": "Juan Perez", "from": "Rita Asturia", "timeToLifeSec": 45}' \
http://$IP_ADDRESS_POD:$PORT/DevOps
```

Having the following output:

```bash
{
  "message": "Hello Juan Perez your message will be send"
}
```

- If we use another HTTP method:

```bash
curl -X POST \
-H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" \
-H "X-JWT-KWY: $JWT_Token" \
-H "Content-Type: application/json" \
-d '{"message": "This is a test", "to": "Juan Perez", "from": "Rita Asturia", "timeToLifeSec": 45}' \
https://ecf7-$NGROK-Public-Address-IP.ngrok-free.app/DevOps
```

It will return "ERROR":

```bash
ERROR
```

Within the microservice running in the container, it returns:

```bash
 * Serving Flask app 'devops'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-062-598
172.17.0.1 - - [21/Oct/2023 08:54:02] "POST /DevOps HTTP/1.1" 200 -
172.17.0.1 - - [21/Oct/2023 08:55:43] "GET /DevOps HTTP/1.1" 405 -
172.17.0.1 - - [21/Oct/2023 08:56:13] "PUT /DevOps HTTP/1.1" 405 -
172.17.0.1 - - [21/Oct/2023 08:56:32] "DELETE /DevOps HTTP/1.1" 405 -
172.17.0.1 - - [21/Oct/2023 08:56:46] "PATCH /DevOps HTTP/1.1" 405 -
172.17.0.1 - - [21/Oct/2023 08:56:56] "POST /DevOps HTTP/1.1" 400 -
172.17.0.1 - - [21/Oct/2023 08:58:10] "POST /DevOps HTTP/1.1" 400 -
172.17.0.1 - - [21/Oct/2023 08:59:45] "POST /DevOps HTTP/1.1" 200 -
```

## How to run

We use the necessary context for Kubernetes:

```bash
minikube stop
minikube start
kubectl config use-context docker-desktop
kubectl config get-contexts
```

We set up the ports using a service:

```bash
kubectl apply -f .\kubernetes\microservice-service.yml
kubectl get services
```

We deploy on Kubernetes for load balancing across 2 pods:

```bash
kubectl describe deployment microservice-deployment
kubectl get deployments
kubectl get pods
```

## Updates

- **22-10-2023**: Refactoring and redesign the project for Unit Test. Reviewed by [Oscar Macias]![chat].

## Support Contact

For questions or issues, please contact on [LinkedIn]![social] or by [e-mail]![mail]. Also, check out our [Python Wiki]![wiki].

[schema]: ./src/img/schema.png

**[chat]: <https://wa.me/573058288031>**

**[mail]: <mailto:omaciasnarvaez@gmail.com>**

**[social]: <https://www.linkedin.com/in/omaciasd/>**

**[wiki]: <https://github.com/OMaciasd/Microservices>**
