# faas_script
The very first script to control the workload for serverless platform.

## Configuration
In ~/.ssh/config, add line:

    ~~~
    Host *.amazonaws.com
	   IdentityFile ~/.ssh/[private key]
    ~~~

## Deployment

### HPA

Edit metric service deployment as in https://blog.csdn.net/ygqygq2/article/details/82971338

    ~~~
    containers:
    - name: metrics-server
      args:
      - --kubelet-preferred-address-types=InternalIP,Hostname,InternalDNS,ExternalDNS,ExternalIP
      - --kubelet-insecure-tls
    ~~~
