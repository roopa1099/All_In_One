## EC2

1. Virtual server on aws datacenter.
2. EC2 are attached to network via Elastic Network Interface ENI
3. EBS :L Elastic bean stalk : Storage for .
4. EC2 instance runs on servers in AWS datacenter, many EC2 can run on 1 server
5. We can provision EC2 based on different combination of resource optimization.
6. EC2 instance can have private as well as can have public subnets

7. ENI = virtual network cable + IP address for an EC2 instance
8. Elastic Network Adapter (ENA)

        ENA is a faster, modern version of the network card.
        AWS created ENA to handle:
        Very high speed
        Low latency
        Lots of data at once
9. Elastic Fabric Adapter (EFA)

    EFA is for super-fast communication between servers.
    Used mainly for:
        Machine learning
        High-performance computing (HPC)
        Scientific simulations
10. EBS should be in same avl zone as ec2 instance to which it is attached.
11. In EBS volume is attached overr network.

12. EBS Multi-Attach (very specific case)
        - Volume type is io1 or io2
        - Instances are in the same Availability Zone
        - Instances are Nitro-based( modern EC2 servers built on AWS’s Nitro system.) 
        - You use a cluster-aware file system (like Oracle RAC) ( A cluster-aware file system knows that multiple servers are using the same disk, i.e. manages concurrency)

13. EC2 itself can have its own temporary storage, but it’s important to understand Instance Store is local storage physically attached to the EC2 server.

14. AMI : Amazon Machine Image : Which OS for EC2, defines configuration of EC2
15. EC2 Key: Pair :
16. Inbound-Outbound rules:

17. IAM roles are better than access keys for EC2 because they are temporary, automatically rotated, and cannot be accidentally leaked or reused outside AWS.
        Access keys are static secrets.
        Static secrets + servers = eventual security incident.